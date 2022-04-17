import streamlit as st
from datetime import time, datetime

st.header('st.slider()')

st.subheader("Slider")

age = st.slider(label="How old are you?", min_value=0, max_value=130, value=25, step=1)

st.write(f"I'm **{age}** years old")

st.subheader("Range Slider")

range_ = st.slider(label='Select a range of values', min_value=0.0, max_value=100.0, value=(25.00, 75.00))
st.write(f"The range of slider: **{range_}**")

st.subheader("Range Time Slider")
time_range = st.slider(label="Schedule your appointment:",
                        min_value=time(00, 00),
                        max_value=time(23, 59),
                        value=(time(9, 30), time(13, 45)))
st.write(f"You're scheduled for: {time_range}")

st.subheader("Datetime Slider")
date_slidier = st.slider(label="When do you start?",
                        min_value=datetime(2020, 1, 1, 9, 30),
                        format="MM/DD/YY - hh:mm")
st.write(f"Start time: {date_slidier}")