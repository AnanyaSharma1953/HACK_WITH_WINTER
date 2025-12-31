from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import SignalModel
from data_simulator import generate_data

app = FastAPI(title="SignalLock API")

# Enable CORS (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SignalModel()
data = generate_data()

@app.get("/")
def home():
    return {"message": "SignalLock backend running"}

@app.post("/train")
def train():
    model.train(data)
    return {"status": "Model trained successfully"}

@app.get("/analyze")
def analyze():
    scores, anomalies = model.predict(data)
    results = []

    for i in range(len(scores)):
        results.append({
            "index": i,
            "anomaly_score": round(scores[i], 3),
            "status": "ANOMALY" if anomalies[i] == -1 else "NORMAL"
        })

    return results
