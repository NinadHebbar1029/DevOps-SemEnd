import sys
import os

# Add the src/ directory itself to sys.path so sibling modules
# (like preprocess.py) can be imported directly, regardless of
# the working directory uvicorn is launched from.
_SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if _SRC_DIR not in sys.path:
    sys.path.insert(0, _SRC_DIR)

import joblib
from preprocess import clean_text

_BASE_DIR = os.path.dirname(_SRC_DIR)  # parent of src/ == project root

# =========================================================
# LOAD TRAINED FILES
# =========================================================

model = joblib.load(os.path.join(_BASE_DIR, "models", "best_model.pkl"))

vectorizer = joblib.load(
    os.path.join(_BASE_DIR, "models", "vectorizer.pkl")
)

label_encoder = joblib.load(
    os.path.join(_BASE_DIR, "models", "label_encoder.pkl")
)


# =========================================================
# EMOTION PREDICTION FUNCTION
# =========================================================

def predict_emotion(text):
    text = clean_text(text)
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    emotion = label_encoder.inverse_transform(prediction)[0]
    return emotion


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":
    sample_text = "I feel happy today"
    result = predict_emotion(sample_text)
    print("Predicted Emotion:", result)