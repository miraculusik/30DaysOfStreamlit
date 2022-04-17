import streamlit as st
import pandas as pd
import numpy as np

st.header("st.selectbox()")


draw = st.selectbox("Select the graph:", ('chart_1', 'chart_2', 'chart_3'))

if "chart_1" in draw:
    data = pd.DataFrame(
        np.random.randn(30, 3),
        columns=['a', 'b', 'c']
        )
    st.line_chart(data)
elif "chart_2" in draw:
    data2 = pd.DataFrame(
        np.random.rand(50, 4),
        columns=[f"Column {i+1}" for i in range(4)]
        )
    st.line_chart(data2)    
elif "chart_3" in draw:
    data3=pd.DataFrame(
        np.random.randn(100, 5),
        columns=[f"Column {i+1}" for i in range(5)])
    st.line_chart(data3)
