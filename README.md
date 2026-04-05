# THE_AI_BET

AIbet is a multi-agent sports and racing intelligence system built to generate structured, traceable, high-confidence predictions across multiple sports and racing codes.

## Purpose

This repository is the foundation for building a 20-agent operating system that analyzes data, reviews context, incorporates video intelligence, and passes predictions through a strict chain of command before final delivery.

The goal is not random model outputs.

The goal is:
- better prediction accuracy
- cleaner data interpretation
- stronger bias detection
- structured confidence scoring
- full traceability from source agent to final output

---

## System Vision

AIbet will operate as a layered intelligence engine.

### Core Analysis Layer
15 dedicated analysis agents split across:
- Horse Racing
- Greyhounds
- AFL
- NRL
- UFC
- NBA
- Soccer
- NFL

Each agent will analyze its own domain using:
- historical data
- raw statistics
- market odds
- bias models
- event context

Each agent will output:
- predictions
- confidence score
- structured reasoning
- risk flags

### Supervisor Layer
A supervisor agent will collect and compare all underlying outputs, identify consensus and conflict, and produce a refined prediction view.

### Video Intelligence Layer
Video AI will review highlights, previews, and relevant footage to extract additional signals such as:
- body language
- player condition
- tactical shape
- contextual performance indicators

### Consensus Engine
A consensus engine will combine supervisor output and video intelligence to filter weak edges and produce cleaner final predictions.

### Sports and Racing Chief
A final decision authority will review all output and approve or override only when justified by system evidence.

### Delivery Layer
DC will receive finalized outputs, format them for platform use, and log them to the ledger for hit-rate, accuracy, and ROI tracking.

---

## Chain of Command

Core Agents  
→ Supervisor  
→ Video Intelligence Input  
→ Consensus Engine  
→ Sports and Racing Chief  
→ DC  
→ Platform / Ledger

---

## Core Principles

- No random agent behaviour
- No unnecessary looping
- No unstructured outputs
- No black-box predictions
- No wasted compute
- Full role separation
- Full traceability
- Cost discipline at every level

---

## Repository Structure

Initial structure:

- README.md — repository overview
- SYSTEM_ARCHITECTURE.md — high-level system design
- AGENT_ROLES.md — detailed breakdown of each agent
- OUTPUT_SCHEMA.json — standard output format for all agents
- DATA_PIPELINE.md — data sources and movement through system
- TASK_QUEUE.md — how tasks are assigned and processed

Future structure may include:

- /agents
- /schemas
- /pipelines
- /logs
- /consensus
- /video-intelligence

---

## Sports Coverage

Current intended coverage:
- Horse Racing
- Greyhounds
- AFL
- NRL
- UFC
- NBA
- Soccer
- NFL

---

## Immediate Build Priorities

1. Lock architecture
2. Define all agent roles
3. Create standardized output schema
4. Define input pipelines
5. Build consensus flow
6. Connect final outputs to ledger logging
7. Begin controlled testing by sport

---

## Mission

Build AIbet into a premium sports and racing intelligence platform with disciplined agent orchestration, strong prediction logic, and evidence-backed outputs.
