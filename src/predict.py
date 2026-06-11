import os
import joblib
import traceback

try:
    from src.preprocess import clean_text
except Exception as e:
    print("================ ERROR IMPORTING PREPROCESS ================")
    traceback.print_exc()
    print("============================================================")
    raise

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =========================================================
# LOAD TRAINED FILES
# =========================================================

try:
    model = joblib.load(os.path.join(BASE_DIR, "models", "best_model.pkl"))
    vectorizer = joblib.load(
        os.path.join(BASE_DIR, "models", "vectorizer.pkl")
    )
    label_encoder = joblib.load(
        os.path.join(BASE_DIR, "models", "label_encoder.pkl")
    )
except Exception as e:
    print("================ ERROR LOADING MODELS ================")
    traceback.print_exc()
    print("======================================================")
    raise


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

if __name__ == "__main__":
    sample_text = "I feel happy today"
    result = predict_emotion(sample_text)
    print("Predicted Emotion:", result)