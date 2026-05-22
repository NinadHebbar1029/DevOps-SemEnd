import joblib

from preprocess import clean_text


# =========================================================
# LOAD TRAINED FILES
# =========================================================

model = joblib.load("models/best_model.pkl")

vectorizer = joblib.load(
    "models/vectorizer.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
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