import streamlit as st
import pandas as pd
import numpy as np

st.header("Line Chart")

data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=['a', 'b', 'c']
    )

st.line_chart(data)


data2 = pd.DataFrame(
    np.random.rand(100, 5),
    columns=[f"Column {i+1}" for i in range(5)]
    )
st.dataframe(data2.describe())
st.line_chart(data2)
st.line_chart(data2.T)