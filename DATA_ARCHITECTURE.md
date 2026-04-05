# AIbet Data Architecture

Unified data infrastructure for multi-sport prediction system.

## Directory Structure

```
/data
├── /raw                    # Source data from scrapers/APIs
│   ├── /nba
│   ├── /ufc
│   ├── /afl
│   ├── /nrl
│   ├── /racing
│   ├── /greyhounds
│   ├── /nfl
│   └── /soccer
├── /processed              # Cleaned, normalized data
│   ├── /daily
│   └── /historical
├── /predictions            # Agent-ready prediction packs
│   ├── /daily              # Today's events
│   └── /archive            # Historical predictions
├── /models                 # Trained model artifacts
└── /ledger                 # Bet tracking & ROI

/agents
├── /core                   # 15 sport-specific agents
│   ├── /racing
│   ├── /ufc
│   ├── /nba
│   └── ...
├── /supervisor             # Aggregation layer
├── /consensus              # Final prediction engine
└── /chief                  # Decision authority

/schemas
├── prediction.schema.json  # Universal output format
├── event.schema.json       # Event data structure
└── agent-output.schema.json # Agent submission format

/pipelines
├── /scrapers               # Data collection scripts
├── /transformers           # Data normalization
└── /exporters              # Agent feed generators

/api                        # Optional: REST API layer
├── /v1
│   ├── /predictions
│   ├── /events
│   └── /agents

/config
├── sports.yaml             # Sport-specific settings
├── agents.yaml             # Agent configurations
└── data-sources.yaml       # API endpoints, credentials
```

## Data Flow

```
External APIs → Raw Data → Processed → Prediction Packs → Agents → Output
     ↑              ↓           ↓              ↓             ↓       ↓
  Scraper      Validator   Normalizer    Pack Builder   Analyze  Ledger
```

## Key Files

| File | Purpose |
|------|---------|
| `/data/predictions/daily/YYYY-MM-DD.json` | All today's events |
| `/data/predictions/daily/{sport}/` | Sport-specific packs |
| `/schemas/prediction.schema.json` | Universal format |
| `/pipelines/exporters/agent-feed.py` | Generates agent inputs |

## Usage

```python
from aibet.data import PredictionPack

# Load today's NBA games
pack = PredictionPack.load('nba', date='2026-04-06')

# Get agent-ready format
agent_input = pack.for_agent('nba-specialist')
```
