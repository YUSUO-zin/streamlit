import streamlit as st

st.header('I am trying my first button ever in streamlit')

if st.button('say hello'):
     st.write('Oh, hii!!!')
else:
     st.write('Okey, goodbye')
