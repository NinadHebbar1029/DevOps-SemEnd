import sys
import os

# Ensure the root directory is on the path regardless of working directory
_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if _ROOT_DIR not in sys.path:
    sys.path.insert(0, _ROOT_DIR)

# Ensure src/ is also on the path so submodules inside src/ can import each other
_SRC_DIR = os.path.join(_ROOT_DIR, "src")
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.predict import predict_emotion

app = FastAPI(title="MindEase API")

# Setup CORS to allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmotionRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotion: str
    reply: str

responses = {
    "sadness": "I'm here for you. Things can improve.",
    "joy": "That's wonderful to hear!",
    "anger": "Take a moment to breathe calmly.",
    "fear": "You are safe. Try grounding yourself.",
    "love": "Connection and care are important."
}

@app.get("/")
def root():
    return {"message": "MindEase API is running"}

@app.post("/predict", response_model=EmotionResponse)
def predict(request: EmotionRequest):
    emotion = predict_emotion(request.text)
    reply = responses.get(emotion, "I understand your feelings.")
    return EmotionResponse(emotion=emotion, reply=reply)
