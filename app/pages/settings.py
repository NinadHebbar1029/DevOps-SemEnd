import streamlit as st

st.title("⚙️ Settings")

# =========================
# INIT STATE
# =========================
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "notifications" not in st.session_state:
    st.session_state.notifications = False

if "reminder" not in st.session_state:
    st.session_state.reminder = False


# =========================
# UI (IMPORTANT FIX HERE)
# =========================

theme = st.selectbox(
    "Theme",
    ["Dark", "Light", "Purple"],
    index=["Dark", "Light", "Purple"].index(st.session_state.theme)
)

notifications = st.checkbox(
    "Enable Notifications",
    value=st.session_state.notifications
)

reminder = st.checkbox(
    "Daily Mood Reminder",
    value=st.session_state.reminder
)


# =========================
# SAVE BUTTON (THIS IS KEY)
# =========================
if st.button("Save Settings"):

    st.session_state.theme = theme
    st.session_state.notifications = notifications
    st.session_state.reminder = reminder

    st.success("Settings Saved ✅")

    st.write("### Current Settings")
    st.json(st.session_state)