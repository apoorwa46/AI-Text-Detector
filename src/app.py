from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# ⭐ VERY IMPORTANT — CORS FIX ⭐
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (simple for local dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/ai_detector.joblib")

class InputText(BaseModel):
    text: str

@app.post("/detect")
def detect(data: InputText):
    prob = model.predict_proba([data.text])[0][1] * 100
    label = "AI-generated" if prob >= 50 else "Human-written"

    return {
        "label": label,
        "probability": round(prob, 2)
    }

@app.get("/")
def home():
    return {"message": "API running"}
