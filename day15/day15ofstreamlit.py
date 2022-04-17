import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
st.markdown('---')

st.subheader("Sigma Formula")
sigma = r'\color{orange}\sigma (sigma)= \color{white}\frac{1}{(1+e^{-z})}'
st.latex(sigma)

st.markdown('---')
st.subheader("Regularization")
regularization = r'''
j(\Theta) = \frac{1}{2m}\left [ \sum_{i=1}^{m} 
(h_\theta(x^{i})-y^{i} ))^2 + 
\color{orange}\lambda\sum_{j=1}^{n} \theta^2_j \right]
'''
st.latex(regularization)
