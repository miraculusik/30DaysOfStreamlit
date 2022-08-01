import streamlit as st
import time

st.title('st.progress')

with st.sidebar.expander('Abouth this app'):
    st.write('You cannow display the progress of your calculations in a Streamlit app with the `st.progress` command.')


my_bar = st.progress(0)
side_my_bar = st.sidebar.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)
    side_my_bar.progress(percent_complete + 1)

st.sidebar.snow()
