import os
import joblib

from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =========================================================
# LOAD TRAINED FILES
# =========================================================

model = joblib.load(os.path.join(BASE_DIR, "models", "best_model.pkl"))

vectorizer = joblib.load(
    os.path.join(BASE_DIR, "models", "vectorizer.pkl")
)

label_encoder = joblib.load(
    os.path.join(BASE_DIR, "models", "label_encoder.pkl")
)


# =========================================================
# EMOTION PREDICTION FUNCTION
# =========================================================

def predict_emotion(text):

    # CLEAN INPUT TEXT
    text = clean_text(text)

    # CONVERT TO TF-IDF VECTOR
    vector = vectorizer.transform([text])

    # PREDICT EMOTION
    prediction = model.predict(vector)

    # CONVERT LABEL TO EMOTION NAME
    emotion = label_encoder.inverse_transform(
        prediction
    )[0]

    return emotion


# =========================================================
# TEST
# =========================================================

sample_text = "I feel happy today"

result = predict_emotion(sample_text)

print("Predicted Emotion:", result)