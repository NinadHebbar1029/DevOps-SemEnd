import streamlit as st


# =========================================================
# PAGE TITLE
# =========================================================

st.title("🧘 Mental Wellness Exercises")


# =========================================================
# EXERCISE SELECTION
# =========================================================

exercise = st.selectbox(
    "Choose Exercise",

    [
        "Breathing",
        "Meditation",
        "Positive Affirmations",
        "Journaling"
    ]
)


# =========================================================
# EXERCISE RESPONSES
# =========================================================

if exercise == "Breathing":

    st.info(
        "Inhale for 4 seconds, hold for 4 seconds, exhale for 4 seconds."
    )

elif exercise == "Meditation":

    st.info(
        "Close your eyes and focus on your breathing for 5 minutes."
    )

elif exercise == "Positive Affirmations":

    st.success(
        "You are capable, strong, and improving every day."
    )

elif exercise == "Journaling":

    st.write(
        "Write 3 things you are grateful for today."
    )