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

SignalLock is an AI-driven early warning platform that detects silent, gradual failures in infrastructure systems (motors, servers, HVAC, UPS, pumps, etc.) before breakdowns occur.

Most infrastructure failures develop slowly through rising vibration, irregular power draw, thermal drift, or network instability. Traditional monitoring systems detect problems only after damage begins.

SignalLock learns what “normal” looks like for each system and flags behavioral drift — the earliest indicator of failure.

> We don’t wait for systems to fail. We detect when they start behaving differently.

---

## ❗ Problem Statement

Modern infrastructure machines fail gradually. Failures can cause downtime, financial loss, safety risks, and service disruption.

Typical failure patterns:
- Rising vibration in motors  
- Irregular power consumption  
- Thermal drift  
- Network latency instability  

Current monitoring systems:
- Use static thresholds  
- Require expensive hardware  
- Depend on manual inspection  
- Detect issues only after damage begins  

**Gap:** No accessible AI system that learns system-specific behavior and detects early drift automatically.

---

## 💡 Proposed Solution

SignalLock is an **unsupervised ML platform** that continuously learns system behavior and detects anomalies relative to its historical baseline.

**Core Capabilities**
- Learns normal behavior patterns  
- Detects early behavioral drift  
- Assigns anomaly confidence scores  
- Explains which signals changed  
- Sends proactive alerts  
- Visualizes system health  

---

## 🏗 System Architecture & Flow

Data Sources (Sensors/CSV/Logs)
│
▼
Ingestion API (FastAPI)
│
▼
Streaming Queue (Redis)
│
▼
Time-Series Database (PostgreSQL/TimescaleDB)
│
▼
ML Engine (Autoencoder + Isolation Forest + Drift Detection)
│
▼
Anomaly Scoring
│
▼
Alert Engine (Email/Webhooks)
│
▼
Web Dashboard (React)

yaml
Copy code

---

## 🔄 Data Flow

Sensor Data
│
▼
Ingestion API
│
▼
Streaming Queue
│
▼
Preprocessing Layer
│
▼
Baseline Model Training
│
▼
Anomaly Detection
│
▼
Health Score Engine
│
▼
Alerts + Dashboard

yaml
Copy code

---

## 🔁 System Flow

Start
│
▼
Collect Sensor Data
│
▼
Store in Database
│
▼
Train Baseline Model
│
▼
Detect Drift & Anomalies
│
▼
Predict Failure Risk
│
▼
Trigger Alerts
│
▼
Visualize Health Score
│
▼
End

yaml
Copy code

---

## ⚙ How the System Works

1. Sensors or CSV feeds send time-series data  
2. FastAPI ingestion service receives the data  
3. Data is streamed via Redis  
4. Stored in PostgreSQL / TimescaleDB  
5. Autoencoder learns normal patterns  
6. Drift detector monitors slow degradation  
7. Anomaly scorer assigns confidence scores  
8. Alert engine triggers early warnings  
9. Dashboard visualizes health and trends  
10. Feedback loop improves ML models continuously  

---

## 🚀 Scalability & Reliability

### Growth Handling

| Component | Scaling Strategy |
|----------|------------------|
| Ingestion API | Docker horizontal scaling |
| Queue | Redis cluster |
| Database | Partitioned time-series DB |
| ML Engine | Worker pool |
| Dashboard | CDN hosting |
| Alerts | Retry + deduplication |

### Reliability

- Queue buffering for traffic spikes  
- Stateless services for failover  
- Model fallback rules  
- Alert deduplication  
- Batched database writes  

---

## 👩‍💻 Team Contributions

### Shruti — Backend & Architecture
- System design  
- FastAPI ingestion API  
- Database schema  
- Docker deployment  

### Anirudh — Machine Learning
- Autoencoder model  
- Drift detection  
- Anomaly scoring  
- Risk prediction  

### Ananya — Frontend
- React dashboard  
- Health score UI  
- Anomaly charts  

### Rohan — Data & Simulation
- Sensor simulator  
- Failure scenario generator  
- Dataset preparation  

---

## 🗂 Repository Structure

SignalLock/
├── backend/ # FastAPI ingestion, APIs
├── ml/ # ML models, training scripts
├── simulator/ # Sensor simulation scripts
├── frontend/ # React dashboard
├── infra/ # Docker, deployment scripts
├── research/ # Research notes and papers
├── demo/ # Demo videos or recordings
└── README.md

yaml
Copy code

---

## 🧪 Prototype

- FastAPI ingestion service  
- ML anomaly detector  
- Sensor simulator  
- Minimal dashboard  

---

## 🎥 Demo

Demo video link:  
[https://drive.google.com/your-demo-link](https://youtu.be/6HwBKlUHTRU)

---

## 📚 Research Notes

- Predictive Maintenance using Machine Learning  
- Time-Series Anomaly Detection  
- Drift Detection Algorithms  
- Autoencoders for Fault Detection  

---

## 🏁 Conclusion

SignalLock is a real-world, scalable AI platform that prevents infrastructure failures before they happen.  

It demonstrates:  
- Deep system design  
- Real-world relevance  
- AI-driven intelligence  
- Production-grade architecture  
- Scalable engineering  

---

## ❤️ Built By

**Team SignalLock**  
Shruti • Anirudh • Ananya • Rohan
