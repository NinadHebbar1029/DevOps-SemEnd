import streamlit as st
import pandas as pd
import plotly.express as px


# =========================================================
# PAGE TITLE
# =========================================================

st.title("📈 Mood History")


# =========================================================
# SAMPLE MOOD DATA
# =========================================================

moods = pd.DataFrame({

    "Day": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ],

    "Mood Score": [
        5,
        6,
        4,
        8,
        7,
        9,
        6
    ]
})


# =========================================================
# CREATE LINE CHART
# =========================================================

fig = px.line(
    moods,
    x="Day",
    y="Mood Score",
    markers=True,
    title="Weekly Mood Trend"
)


# =========================================================
# DISPLAY CHART
# =========================================================

st.plotly_chart(
    fig,
    use_container_width=True
)