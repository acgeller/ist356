import streamlit as st

st.title('Order Processor')

#inititalize variables 
total = 0.0
count = 0

#input
file = st.file_uploader('Upload Text File: ', type = ['txt'])

#Process
if file is not None:
    for line in file:
        try:
            total += float(line.decode('utf-8').strip())
            count += 1
        except ValueError:
            st.error(f"Invalid value in file: {line.decode('utf-8').strip()}")

#output
st.write(f'Total Amount: ${total}')
st.write(f'Total Orders: {count}')