import streamlit as st

st.title('Order Tracker')

#Inititalize variables
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.history = []

#Inputs
amount = st.number_input('Order Amount:', value = st.session_state.amount)
total_button = st.button('Calculate Total', type = "primary")
clear_button = st.button('Clear')

#Process (avoid ouputting, just manipulate data)
if total_button:
    st.session_state.total += amount
    st.session_state.history.append(amount)

if clear_button:
    st.session_state.total = 0
    st.session_state.history = []

#Ouputs
st.write(f'Total Ordered: {st.session_state.total}')
st.write(f'History: {st.session_state.history}')