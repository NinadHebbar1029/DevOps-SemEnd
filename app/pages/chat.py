import streamlit as st
import joblib
import re


# =========================================================
# LOAD MODEL FILES
# =========================================================

model = joblib.load(
    "models/best_model.pkl"
)

vectorizer = joblib.load(
    "models/vectorizer.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
)


# =========================================================
# TEXT CLEANING FUNCTION
# =========================================================

def clean_text(text):

    text = str(text).lower()

    text = text.replace(
        "don't",
        "not"
    )

    text = text.replace(
        "dont",
        "not"
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    return text


# =========================================================
# PAGE UI
# =========================================================

st.title("🧠 AI Mental Health Chat")


# =========================================================
# USER INPUT
# =========================================================

user_input = st.text_area(
    "How are you feeling today?",
    height=150
)


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button("Analyze Emotion"):

    # CLEAN TEXT
    cleaned = clean_text(user_input)

    # CONVERT TO VECTOR
    vector = vectorizer.transform(
        [cleaned]
    )

    # PREDICT
    prediction = model.predict(vector)

    # DECODE LABEL
    emotion = label_encoder.inverse_transform(
        prediction
    )[0]

    # DISPLAY RESULT
    st.success(
        f"Detected Emotion: {emotion}"
    )

    # RESPONSE SECTION
    if emotion in ["sadness", "fear"]:

        st.warning(
            "Try taking deep breaths and journaling."
        )

    elif emotion == "joy":

        st.balloons()

    elif emotion == "anger":

        st.error(
            "Consider calming exercises."
        )