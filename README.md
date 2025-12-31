# SignalLock

**AI-powered Early Warning System for Silent Infrastructure Failures**

---

## Overview

SignalLock is an AI-driven system that detects **silent, gradual failures** in infrastructure (water pumps, electrical panels, servers, motors, UPS systems) *before* breakdowns occur.

Instead of relying on fixed thresholds, SignalLock **learns normal behavior patterns** from time-series signals and flags **behavioral drift** — the earliest indicator of failure.

> *"We don't wait for systems to fail. We detect when they start behaving differently."*

---

## Problem Statement

Most infrastructure failures are **not sudden**. They emerge slowly as:

* Rising vibration in motors
* Irregular power draw
* Thermal drift
* Network latency instability

Current monitoring systems:

* Use static thresholds
* Require expensive hardware
* Depend on manual inspections
* Detect issues **after damage begins**

This leads to avoidable downtime, financial loss, and safety risks.

---

## Why Existing Solutions Fall Short

| Existing Approach    | Limitation                |
| -------------------- | ------------------------- |
| Rule-based alerts    | Miss gradual degradation  |
| Industrial IoT tools | Costly & inaccessible     |
| Dashboards           | No intelligence           |
| Predictive tools     | Need labeled failure data |

**Key Gap:** No affordable, learning-based system that works with *small, noisy, unlabeled data*.

---

## Proposed Solution

SignalLock applies **unsupervised machine learning** to continuously learn what "normal" looks like for a system and detect **anomalies relative to its own past behavior**.

### Core Capabilities

* Learns system-specific baselines
* Detects early drift patterns
* Assigns anomaly confidence scores
* Explains which signals changed

---

## System Architecture (High Level)

```
┌──────────────┐
│ Data Source  │  (CSV / Sensors / Logs)
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Ingestion API    │  (FastAPI)
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Time-Series DB   │  (Postgres / Timescale)
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ ML Engine        │
│ - Autoencoder    │
│ - IsolationForest│
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Anomaly Scorer   │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Alert & Explain  │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Web Dashboard    │
└──────────────────┘
```

---

## Data Flow Diagram (DFD)

```
[Sensor Data]
      ↓
[Data Ingestion API]
      ↓
[Preprocessing Layer]
      ↓
[Baseline Model Training]
      ↓
[Anomaly Detection]
      ↓
[Health Score Engine]
      ↓
[Alerts + Dashboard]
```

---

## Round 1 Features (Prototype Scope)

* Time-series data ingestion (CSV or stream)
* Self-learning baseline model
* Anomaly score visualization
* Early warning alerts
* Signal-level explainability
* Minimal React dashboard

**No hardware required. No paid APIs.**

---

## Tech Stack

**Backend:** Python, FastAPI

**ML:**

* Autoencoders (PyTorch)
* Isolation Forest (scikit-learn)
* Rolling window anomaly scoring

**Database:** PostgreSQL / TimescaleDB

**Frontend:** React, Recharts

**Deployment:** Docker

---

## Round 2 Expansion Plan

* Multi-site behavior comparison
* Root-cause correlation engine
* Edge deployment (Raspberry Pi)
* Federated learning (privacy-safe)
* Failure probability forecasting
* WhatsApp/SMS alert integration
* Governance & municipal use cases

---

## Why SignalLock Wins

* Solves a **non-obvious but critical problem**
* Strong AI + systems depth
* Works with small, unlabeled data
* Scales from 1 building to 10,000 sites
* Clear demo + clear future roadmap
* Extremely low plagiarism risk

---

## 30-Second Pitch

> "Most infrastructure failures are silent. SignalLock learns normal system behavior and detects early degradation before breakdowns occur. We move from reactive monitoring to proactive intelligence."

---

## Team & Domain

**Domain:** AI / ML · Open Innovation

**Team Size:** 4

---

*Built for Hack The Winter – Angry Bird Edition*

