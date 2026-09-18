import streamlit as st

st.title("Streamlit Interaction: linear")

# setup
name = st.text_input("Who are you?")
hi_clicked = st.button('Say Hi!', type = "primary")
clear_clicked = st.button('Clear', type = "primary")

# interactions
if hi_clicked:
    if name:
        st.success(f"Hello, {name}", icon="👍")
    else:
        st.error(f"I can't say hello, if you don't tell me your name!", icon="💣")

if clear_clicked:
    name = None 
