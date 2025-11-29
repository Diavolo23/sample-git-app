import streamlit as st
st.title('CampusX')
col1, col2 = st.columns(2)

with col1:
    st.image('sss.jpeg')
with col2:
    st.header('Campus X is online')

st.header("courses")
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')
st.subheader('DSP')
st.sidebar.title('menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career section 
- Login
""")

st.sidebar.selectbox('Select one',['teacher','student'])
st.sidebar.button('select')

st.title("Hello teacher")
