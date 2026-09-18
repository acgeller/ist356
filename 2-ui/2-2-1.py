import streamlit as st

st.title("2-2-1 Area & Perimeter Calculator")

length = st.number_input("What is the length of your rectangle?", min_value=0)
width = st.number_input("What is the width of your rectangle?", min_value=0)

calculate = st.button("Calculate Area & Perimeter", type="primary")
clear_button = st.button("Clear", type="primary")

if calculate:
    perimeter = length * 2 + width * 2
    area = length * width
    st.write(f"The area of your rectangle is {area} and the perimeter is {perimeter}.")

if clear_button:
    length = 0
    width = 0
    st.write("Inputs cleared. Please enter new values.")