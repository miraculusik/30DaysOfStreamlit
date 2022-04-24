import streamlit as st

st.title('Coffee Order')

st.header('1. Example of using `with` notation')
st.subheader('Coffe machine')

with st.form('my_form'):
    st.write('**Order your coffee**')

    # Input Widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    serving_type_val =  st.selectbox('Serving format', ['Hot', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')
    # Every form must have a submit button

    submitted = st.form_submit_button('Submit')


if submitted:
    st.markdown(f'''
    ☕ You have ordered:
    - Coffe bean: {coffee_bean_val}
    - Coffee roast: {coffee_roast_val}
    - Brewinmg: {brewing_val}
    - Serving_type: {serving_type_val}
    - Milk: {milk_val}
    - Bring own cup: {owncup_val}
    ''')
else:
    st.write('Place your order!')

