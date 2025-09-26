import streamlit as st
from app.core import add

st.title("DS/ML Pro Starter Demo")
st.write("This is a minimal Streamlit app to demo an interactive UI.")
a = st.number_input("a", value=1.0)
b = st.number_input("b", value=2.0)
st.metric("a + b", add(a, b))
