import os
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Mental Health AI",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

css_path = os.path.join(os.path.dirname(__file__), "style.css")

with open(css_path) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
    <h1 style='
        text-align:center;
        color:white;
        font-size:60px;
    '>
        MindEase AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='
        text-align:center;
        color:#dddddd;
    '>
        AI Powered Mental Health Emotion Detection System
    </h3>
    """,
    unsafe_allow_html=True
)

st.image(
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
    use_column_width=True
)

st.write("")
st.write("")


# =========================================================
# FEATURES SECTION
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Supported Emotions",
        "6"
    )

with col2:
    st.metric(
        "Dataset Size",
        "20K+"
    )

with col3:
    st.metric(
        "Best Accuracy",
        "88%"
    )

st.write("")


# =========================================================
# LOGIN SECTION
# =========================================================

st.markdown(
    """
    <div style='
        background:rgba(255,255,255,0.1);
        padding:30px;
        border-radius:20px;
    '>

    <h2 style='
        color:white;
        text-align:center;
    '>
        Login
    </h2>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# INPUT FIELDS
# =========================================================

username = st.text_input(
    "Username"
)

password = st.text_input(
    "Password",
    type="password"
)


# =========================================================
# LOGIN BUTTON
# =========================================================

if st.button("Login"):

    st.success("Login Successful")

    st.info(
        "Use sidebar to navigate pages"
    )