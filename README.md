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

SignalLock is an AI-driven early warning platform that detects silent, gradual failures in infrastructure systems such as water pumps, electrical panels, servers, motors, HVAC units, and UPS systems — before breakdowns occur.

Most infrastructure failures are not sudden. They develop slowly through rising vibration, irregular power draw, thermal drift, or network instability. Traditional monitoring systems detect problems only after damage has already begun.

SignalLock learns what “normal” looks like for every system and flags behavioral drift — the earliest indicator of failure.

> We don’t wait for systems to fail. We detect when they start behaving differently.

---

## ❗ Problem Statement

Modern infrastructure relies on machines that run continuously. Their failures cause downtime, financial loss, safety risks, and service disruption.

Most failures emerge gradually as:
- Rising vibration in motors  
- Irregular power consumption  
- Thermal drift  
- Network latency instability  

Current monitoring systems:
- Use static thresholds  
- Require expensive proprietary hardware  
- Depend on manual inspection  
- Detect issues only after damage begins  

There is no affordable, learning-based system that works with small, noisy, unlabeled data.

---

## 🚫 Why Existing Solutions Fall Short

| Existing Approach | Limitation |
|------------------|------------|
| Rule-based alerts | Miss gradual degradation |
| Industrial IoT tools | Too costly for small institutions |
| Dashboards | No intelligence |
| Predictive tools | Require labeled failure data |

Key Gap:  
No accessible AI system that can learn system-specific behavior and detect early drift automatically.

---

## 💡 Proposed Solution

SignalLock is an unsupervised machine learning platform that continuously learns system behavior and detects anomalies relative to its own historical baseline.

### Core Capabilities
- Learns normal behavior patterns  
- Detects early behavioral drift  
- Assigns anomaly confidence scores  
- Explains which signals changed  
- Sends proactive alerts  
- Visualizes system health  

---

## 🏗 System Architecture

Data Sources (Sensors / CSV / Logs)
│
▼
Ingestion API (FastAPI)
│
▼
Streaming Queue (Redis)
│
▼
Time-Series Database (PostgreSQL)
│
▼
ML Engine (Autoencoder + IF)
│
▼
Anomaly Scoring
│
▼
Alert Engine
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
Preprocessing
│
▼
Baseline Training
│
▼
Anomaly Detection
│
▼
Health Scoring
│
▼
Alerts + Dashboard

yaml
Copy code

---

## 🔁 System Flow

Collect Data → Store Data → Train Model → Detect Drift → Predict Risk → Send Alerts → Visualize Health

yaml
Copy code

---

## ⚙ How the System Works

1. Sensors or CSV feeds send time-series data  
2. FastAPI ingestion service receives data  
3. Data is streamed via Redis  
4. Stored in PostgreSQL  
5. Autoencoder learns normal patterns  
6. Drift detector monitors slow degradation  
7. Anomaly scorer assigns confidence score  
8. Alert engine triggers early warnings  
9. Dashboard visualizes health and trends  

---

## 🚀 Scalability & Reliability

### Growth Handling

| Component | Scaling Strategy |
|----------|------------------|
| Ingestion API | Docker horizontal scaling |
| Queue | Redis cluster |
| Database | Partitioned time-series |
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
├── backend/
├── ml/
├── simulator/
├── frontend/
├── infra/
├── diagrams/
├── research/
├── demo/
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
https://drive.google.com/your-demo-link

---

## 📚 Research Notes

- Predictive Maintenance using Machine Learning  
- Time-Series Anomaly Detection  
- Drift Detection Algorithms  
- Autoencoders for Fault Detection  

---

## 🏁 Conclusion

SignalLock is a real-world, scalable AI platform that prevents infrastructure failures before they happen.

This project demonstrates:
- Deep system design  
- Real-world relevance  
- AI-driven intelligence  
- Production-grade architecture  
- Scalable engineering  

---

## ❤️ Built By

**Team SignalLock**  
Shruti • Anirudh • Ananya • Rohan
