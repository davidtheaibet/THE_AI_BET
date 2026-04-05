#!/bin/bash
# AIbet Data Pipeline Runner
# Orchestrates all data collection and prediction pack generation

set -e

AIBET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DATA_DIR="$AIBET_DIR/data"
LOG_DIR="$AIBET_DIR/logs"

# Create directories
mkdir -p "$DATA_DIR"/{raw,processed,predictions,ledger}
mkdir -p "$LOG_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_DIR/pipeline.log"
}

# NBA Data Collection
run_nba() {
    log "Starting NBA data collection..."
    cd "$AIBET_DIR/../aibet-nba-data" || exit
    source venv/bin/activate
    python src/scrapers/nba_stats_scraper.py --recency
    python src/processors/data_processor.py
    log "NBA data complete"
}

# Generate Prediction Packs
generate_packs() {
    log "Generating prediction packs..."
    cd "$AIBET_DIR/pipelines"
    python3 prediction_pack.py
    log "Prediction packs generated"
}

# Distribute to Agents
distribute() {
    log "Distributing to agents..."
    # Trigger agent processing
    # This could be API calls, message queue, or file watchers
    log "Distribution complete"
}

# Main execution
case "${1:-all}" in
    nba)
        run_nba
        ;;
    packs)
        generate_packs
        ;;
    distribute)
        distribute
        ;;
    all)
        run_nba
        generate_packs
        distribute
        ;;
    *)
        echo "Usage: $0 {nba|packs|distribute|all}"
        exit 1
        ;;
esac

log "Pipeline complete"
