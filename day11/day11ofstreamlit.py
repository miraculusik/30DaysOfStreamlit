import streamlit as st
import pandas as pd
import numpy as np
import random

st.header("st.multiselect()")

options = st.multiselect(
    "What are your favorite colors",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write(f"You selected: {options}")


random_option = st.multiselect(
    "Select Numbers",
    [i for i in range(10)])
st.write(f"Your numbers are {random_option}\
    \nSum : {sum(random_option)}\
    \nMean : {np.mean(random_option):.2f}\
    \nMedian : {np.median(random_option):.2f}")