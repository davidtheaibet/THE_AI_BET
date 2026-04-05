# AIbet Multi-Agent System Architecture

## Overview
This system is a 20-agent structured intelligence engine designed to generate high-confidence sports and racing predictions through layered analysis.

---

## Agent Structure

### 1. Core Analysis Layer (15 Agents)

#### Horse Racing (4)
- Form Analyst
- Track/Bias Analyst
- Tempo/Map Analyst
- Market/Odds Analyst

#### Greyhounds (1)
- Speed/Form + Box Bias Specialist

#### AFL (2)
#### NRL (2)
#### UFC (2)
#### NBA (2)
#### Soccer (1)
#### NFL (1)

Each agent:
- Input: Raw data, historical stats, odds, bias models
- Output:
  - Predictions
  - Confidence score
  - Reasoning
  - Risk flags

---

### 2. Supervisor Layer (1 Agent)

- Aggregates all outputs
- Identifies consensus vs conflict
- Weights predictions based on:
  - Accuracy history
  - Data strength
  - Market edge

---

### 3. Video Intelligence Layer (1 Agent/System)

- Processes highlights and previews
- Extracts:
  - Player condition
  - Body language
  - Tactical insights

---

### 4. Consensus Engine (1 Agent)

- Combines Supervisor + Video signals
- Filters weak predictions
- Outputs final structured predictions

---

### 5. Sports & Racing Chief (1 Agent)

- Final decision authority
- Approves or overrides outputs

---

### 6. Delivery Layer (DC)

- Formats output
- Pushes to platform
- Logs to ledger

---

## Data Flow

Core Agents → Supervisor → Consensus Engine → Chief → DC → Platform

(Video layer feeds into Supervisor + Consensus)

---

## Rules

- No agent-to-agent chatter
- No looping processes
- All outputs structured
- Full traceability required
- Cost efficiency enforced

---

## Next Steps

- Define each agent as a module
- Connect data inputs
- Standardize output format
- Begin testing per sport
