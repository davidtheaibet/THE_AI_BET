# AIbet Agent Output Schema

Standardized format for all agent submissions to the supervisor layer.

## Submission Format

```json
{
  "submission_id": "uuid",
  "agent_id": "nba-specialist-01",
  "agent_type": "core|supervisor|consensus|chief",
  "timestamp": "2026-04-06T12:00:00Z",
  "event_id": "nba_OKC_UTA_20260406",
  
  "analysis": {
    "confidence_score": 0.85,
    "confidence_level": "high|medium|low",
    "prediction": {
      "type": "winner|spread|total|prop",
      "selection": "OKC",
      "line": -5.5,
      "odds": 1.90
    },
    "reasoning": {
      "summary": "Brief explanation",
      "key_factors": [
        "Factor 1 with data",
        "Factor 2 with data"
      ],
      "data_points": {
        "stat_name": "value"
      }
    },
    "risk_flags": [
      "injury_concern",
      "weather_impact",
      "line_movement"
    ]
  },
  
  "model_metadata": {
    "model_version": "1.2.0",
    "data_sources": ["nba_api", "recent_form"],
    "features_used": ["pace", "efficiency", "rest_days"],
    "training_date": "2026-03-15"
  },
  
  "performance_tracking": {
    "agent_historical_accuracy": 0.62,
    "sport_historical_accuracy": 0.58,
    "similar_predictions_count": 45,
    "similar_predictions_win_rate": 0.64
  }
}
```

## Confidence Levels

| Score | Level | Action |
|-------|-------|--------|
| 0.80+ | High | Proceed to consensus |
| 0.60-0.79 | Medium | Flag for review |
| <0.60 | Low | Discard or request more data |

## Risk Flags

- `injury_concern` — Key player questionable/out
- `weather_impact` — Outdoor event, conditions changing
- `line_movement` — Significant market shift
- `low_sample_size` — Insufficient historical data
- `rest_disadvantage` — Back-to-back, travel, etc.
- `motivation_question` — Late season, playoff implications

## Validation Rules

1. All required fields must be present
2. Confidence score must match confidence level ranges
3. Event ID must match master event list
4. Agent ID must be registered in system
5. Timestamp must be within 24h of event

## Submission Endpoint

```bash
POST /api/v1/agent/submit
Content-Type: application/json
X-Agent-ID: {agent_id}
X-API-Key: {key}
```
