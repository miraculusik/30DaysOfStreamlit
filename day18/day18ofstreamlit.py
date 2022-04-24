import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
# Settings
plt.xkcd()
st.set_option('deprecation.showPyplotGlobalUse', False)


# file upload
st.title('st.file_uploader')
st.subheader('Input CSV')

uploaded_file = st.file_uploader('Chose a file')

if uploaded_file is not None:
    global df 
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

else :
    st.info('Upload a CSV file')


col_1, col_2, col_3 = st.columns(3)

col_1.metric('Number of rows', f'{df.shape[0]}')
col_2.metric('Number of columns', f'{df.shape[1]}')
col_3.metric('Sum of NaN', f'{df.isnull().sum().sum()}')

fig = sns.countplot(data=df, y='gender')

st.pyplot(plt.show())