"""
AIbet Prediction Pack Builder
Generates standardized prediction packs for agent consumption.
"""

import json
import os
from datetime import datetime, date
from typing import List, Dict, Optional
from pathlib import Path


class PredictionPack:
    """
    Universal prediction pack for all sports.
    
    Usage:
        pack = PredictionPack(sport='nba', event_date='2026-04-06')
        pack.add_event({...event_data...})
        pack.save()
        
        # Load for agent
        agent_input = pack.for_agent('nba-specialist')
    """
    
    def __init__(self, sport: str, event_date: str = None, version: str = "v1"):
        self.sport = sport
        self.event_date = event_date or date.today().isoformat()
        self.version = version
        self.pack_id = f"{sport}_{self.event_date.replace('-', '')}_{version}"
        self.events = []
        self.generated_at = datetime.utcnow().isoformat() + "Z"
        self.data_sources = []
        
    def add_event(self, event: Dict):
        """Add an event to the pack."""
        self.events.append(event)
        
    def add_data_source(self, source: str):
        """Track data provenance."""
        if source not in self.data_sources:
            self.data_sources.append(source)
            
    def to_dict(self) -> Dict:
        """Export as dictionary."""
        return {
            "pack_id": self.pack_id,
            "sport": self.sport,
            "generated_at": self.generated_at,
            "data_sources": self.data_sources,
            "events": self.events
        }
        
    def to_json(self) -> str:
        """Export as JSON string."""
        return json.dumps(self.to_dict(), indent=2)
        
    def save(self, base_path: str = "./data/predictions") -> str:
        """Save to file system."""
        # Create directories
        sport_dir = Path(base_path) / self.sport
        daily_dir = Path(base_path) / "daily"
        sport_dir.mkdir(parents=True, exist_ok=True)
        daily_dir.mkdir(parents=True, exist_ok=True)
        
        # Save to sport-specific folder
        filepath = sport_dir / f"{self.pack_id}.json"
        with open(filepath, 'w') as f:
            f.write(self.to_json())
            
        # Also save to daily aggregate
        daily_path = daily_dir / f"{self.event_date}.json"
        
        # Load existing daily or create new
        if daily_path.exists():
            with open(daily_path) as f:
                daily = json.load(f)
        else:
            daily = {"date": self.event_date, "sports": {}}
            
        # Add/update this sport
        daily["sports"][self.sport] = {
            "pack_id": self.pack_id,
            "event_count": len(self.events),
            "generated_at": self.generated_at
        }
        
        with open(daily_path, 'w') as f:
            json.dump(daily, f, indent=2)
            
        return str(filepath)
        
    def for_agent(self, agent_id: str) -> Dict:
        """
        Generate agent-specific view of the data.
        Filters and formats based on agent specialization.
        """
        # Base data
        agent_pack = {
            "agent_id": agent_id,
            "pack_id": self.pack_id,
            "sport": self.sport,
            "event_count": len(self.events),
            "generated_at": self.generated_at
        }
        
        # Agent-specific filtering could happen here
        # e.g., only high-confidence events, specific leagues, etc.
        agent_pack["events"] = self.events
        
        return agent_pack
        
    @classmethod
    def load(cls, sport: str, event_date: str = None, base_path: str = "./data/predictions") -> Optional['PredictionPack']:
        """Load an existing prediction pack."""
        event_date = event_date or date.today().isoformat()
        sport_dir = Path(base_path) / sport
        
        # Find latest version
        files = list(sport_dir.glob(f"{sport}_{event_date.replace('-', '')}_*.json"))
        if not files:
            return None
            
        latest = max(files, key=lambda p: p.stat().st_mtime)
        
        with open(latest) as f:
            data = json.load(f)
            
        pack = cls(sport=sport, event_date=event_date)
        pack.pack_id = data['pack_id']
        pack.events = data['events']
        pack.data_sources = data.get('data_sources', [])
        pack.generated_at = data['generated_at']
        
        return pack


class AgentFeed:
    """
    Generates feeds for specific agent types.
    """
    
    def __init__(self, base_path: str = "./data/predictions"):
        self.base_path = Path(base_path)
        
    def get_daily_feed(self, event_date: str = None) -> Dict:
        """Get all sports for a given day."""
        event_date = event_date or date.today().isoformat()
        daily_path = self.base_path / "daily" / f"{event_date}.json"
        
        if not daily_path.exists():
            return {"date": event_date, "sports": {}}
            
        with open(daily_path) as f:
            return json.load(f)
            
    def get_sport_feed(self, sport: str, event_date: str = None) -> Optional[Dict]:
        """Get specific sport pack."""
        pack = PredictionPack.load(sport, event_date, str(self.base_path))
        return pack.to_dict() if pack else None
        
    def get_agent_workload(self, agent_id: str, agent_config: Dict) -> List[Dict]:
        """
        Generate workload for a specific agent.
        Based on agent's sport specialization and capacity.
        """
        workload = []
        
        # Get agent's sports
        sports = agent_config.get('sports', [])
        max_events = agent_config.get('max_daily_events', 20)
        
        for sport in sports:
            pack = PredictionPack.load(sport, base_path=str(self.base_path))
            if pack:
                events = pack.for_agent(agent_id)
                workload.append(events)
                
        # Flatten and limit
        all_events = []
        for w in workload:
            all_events.extend(w.get('events', []))
            
        return all_events[:max_events]


# Example usage
if __name__ == "__main__":
    # Create NBA pack
    pack = PredictionPack(sport='nba', event_date='2026-04-06')
    pack.add_data_source('nba_api')
    pack.add_data_source('recent_form')
    
    # Add sample event
    pack.add_event({
        "event_id": "nba_OKC_UTA_20260406",
        "event_type": "game",
        "datetime": "2026-04-06T19:00:00Z",
        "participants": [
            {"id": "OKC", "name": "Oklahoma City Thunder", "type": "team"},
            {"id": "UTA", "name": "Utah Jazz", "type": "team"}
        ]
    })
    
    # Save
    path = pack.save()
    print(f"Saved to: {path}")
    
    # Load for agent
    loaded = PredictionPack.load('nba', '2026-04-06')
    agent_view = loaded.for_agent('nba-specialist-01')
    print(f"Agent view: {agent_view['event_count']} events")
