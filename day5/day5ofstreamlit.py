import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header('st.write()')
st.markdown('---')

# Example 1
st.write('Hello, *World!* :sunglasses:')
st.markdown('---')

# Example 2
st.write(1234)
st.markdown('---')

# Example 3
df = pd.DataFrame({
    'first_column':[1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})
st.write(df)
st.markdown('---')

# Example 4
st.write('Below is a DataFrame:',df, 'Above is a dataframe.')
st.markdown('---')

# Example 5

df2 = pd.DataFrame(
    np.random.rand(200, 3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)