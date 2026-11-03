import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.title('Exam Scores Pivot Table')
#inputs
row = st.multiselect('Select Row', options = list(exams.columns))
col = st.multiselect('Select Column', options = list(exams.columns))
measure = st.selectbox('Select Measure', options = list(exams.columns))
aggregate = st.selectbox('Select Aggregate', options = ['mean', 'sum', 'count'])

try:
    pivot1 = exams.pivot_table(index = row,
                            columns = col, 
                            values = measure, aggfunc = aggregate)

except ValueError as e:
    st.error(f"Row/Column measure values canot be re-used. Measures must be numbers: {e}")

#output
st.dataframe(pivot1)