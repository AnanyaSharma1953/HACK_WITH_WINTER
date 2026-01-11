# 🚀 SignalLock  
AI-Powered Early Warning System for Silent Infrastructure Failures

---

## 🏆 Hackathon  
**Hack The Winter – Angry Bird Edition**

---

## 👥 Team

| Name     | Role |
|----------|------|
| Shruti   | System Architect & Backend Lead |
| Anirudh  | Machine Learning Engineer |
| Ananya   | Frontend Engineer |
| Rohan    | Data & Simulation Engineer |

---

## 📌 Overview

SignalLock is an AI-driven early warning platform that detects silent, gradual failures in infrastructure systems (motors, servers, HVAC, UPS, etc.) before breakdowns occur.  

Most failures develop slowly (vibration, thermal drift, irregular power draw, network instability). SignalLock learns normal patterns and flags early drift.

> We don’t wait for systems to fail. We detect when they start behaving differently.

---

## ❗ Problem Statement

Modern infrastructure machines fail gradually. Current monitoring systems:  
- Use static thresholds  
- Require expensive hardware  
- Detect issues only after damage occurs  

Key Gap: No accessible AI system that learns system behavior and detects early drift automatically.

---

## 💡 Proposed Solution

SignalLock continuously learns system behavior and detects anomalies relative to its historical baseline.

### Core Capabilities
- Learns normal behavior patterns  
- Detects early behavioral drift  
- Assigns anomaly confidence scores  
- Explains which signals changed  
- Sends proactive alerts  
- Visualizes system health  

---

## 🏗 System Architecture

```mermaid
flowchart TD
    A[Data Sources: Sensors / CSV / Logs] --> B[Ingestion API (FastAPI)]
    B --> C[Streaming Queue (Redis)]
    C --> D[Time-Series Database (PostgreSQL / TimescaleDB)]
    D --> E[ML Engine: Autoencoder + Isolation Forest + Drift Detection]
    E --> F[Anomaly Scoring]
    F --> G[Alert Engine: Email / Webhooks]
    G --> H[Web Dashboard (React)]
    F --> D[Feedback Loop for Model Updates]
🔄 Data Flow
mermaid
Copy code
flowchart TD
    A[Sensor Data] --> B[Ingestion API]
    B --> C[Streaming Queue]
    C --> D[Preprocessing Layer]
    D --> E[Baseline Model Training]
    E --> F[Anomaly Detection]
    F --> G[Health Score Engine]
    G --> H[Alerts + Dashboard]
🔁 System Flow
mermaid
Copy code
flowchart TD
    Start --> Collect[Collect Sensor Data]
    Collect --> Store[Store in Database]
    Store --> Train[Train Baseline Model]
    Train --> Detect[Detect Drift & Anomalies]
    Detect --> Predict[Predict Failure Risk]
    Predict --> Trigger[Trigger Alerts]
    Trigger --> Visualize[Visualize Health Score]
    Visualize --> End
⚙ How the System Works
Sensors or CSV feeds send time-series data

FastAPI ingestion service receives data

Data is streamed via Redis

Stored in PostgreSQL / TimescaleDB

Autoencoder learns normal patterns

Drift detector monitors slow degradation

Anomaly scorer assigns confidence scores

Alert engine triggers early warnings

Dashboard visualizes health and trends

🚀 Scalability & Reliability
Growth Handling
Component	Scaling Strategy
Ingestion API	Docker horizontal scaling
Queue	Redis cluster
Database	Partitioned Time-Series DB
ML Engine	Worker pool
Dashboard	CDN hosting
Alerts	Retry + Deduplication

Reliability
Queue buffering for traffic spikes

Stateless services for failover

Model fallback rules

Alert deduplication

Batched database writes

👩‍💻 Team Contributions
Shruti — Backend & Architecture
System design

FastAPI ingestion API

Database schema

Docker deployment

Anirudh — Machine Learning
Autoencoder model

Drift detection

Anomaly scoring

Risk prediction

Ananya — Frontend
React dashboard

Health score UI

Anomaly charts

Rohan — Data & Simulation
Sensor simulator

Failure scenario generator

Dataset preparation

🗂 Repository Structure
Copy code
SignalLock/
├── backend/
├── ml/
├── simulator/
├── frontend/
├── infra/
├── diagrams/
├── research/
├── demo/
└── README.md
🧪 Prototype
FastAPI ingestion service

ML anomaly detector

Sensor simulator

Minimal dashboard

🎥 Demo
Demo video link:
https://drive.google.com/your-demo-link

📚 Research Notes
Predictive Maintenance using Machine Learning

Time-Series Anomaly Detection

Drift Detection Algorithms

Autoencoders for Fault Detection

🏁 Conclusion
SignalLock is a scalable AI platform that prevents infrastructure failures before they happen.

It demonstrates:

Deep system design

Real-world relevance

AI-driven intelligence

Production-grade architecture

Scalable engineering

❤️ Built By
Team SignalLock
Shruti • Anirudh • Ananya • Rohan
