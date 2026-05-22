import streamlit as st
import plotly.express as px
import pandas as pd
st.title(" Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Total Chats", "254")
col2.metric("Positive Days", "18")
col3.metric("Stress Level", "Low")
emotion_data = pd.DataFrame({
"Emotion": ["Joy","Sadness","Anger","Fear"],
"Count": [50,20,10,15]
})
fig = px.pie(
emotion_data,
names="Emotion",
values="Count",
title="Emotion Distribution"
)
st.plotly_chart(fig, use_container_width=True)