import streamlit as st

st.title("Saying Hello.")
name = st.text_input("And you are?")
age = st.slider("How old are you?", 18,50, value = 18, step = 1)

mybutton = st.button("GO FOR IT", type = "primary")

if mybutton:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")