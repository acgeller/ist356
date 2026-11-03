import streamlit as st
import pandas as pd
import datetime

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls/roster.csv"

roster = pd.read_csv(f"{base}/roster.csv")

weeks = 4
polls = []
start_date = datetime.date(2024, 1, 8)
class_span = datetime.timedelta(days = 7)
for week in range(weeks):
    current_date = start_date + week * class_span
    poll_file = f"{base}/poll-responses-{current_date}.csv"
    poll_data = pd.read_csv(poll_file)
    poll_data['poll_date'] = current_date 
    polls.append(poll_data)

polls_appended = pd.concat(polls)

polls_pivoted = polls_appended.pivot_table(index = 'student_id', 
                                           columns = 'poll_date', 
                                           values = 'answer', 
                                           aggfunc='count').reset_index()

# now melt the data so dates are back in a single column
polls_melted = polls_pivoted.reset_index().melt(id_vars = 'student_id',
                                                var_name = 'poll_date',
                                                value_name = 'count_of_responses')
polls_grouped = polls_melted.groupby('student_id')['count_of_responses']\
    .apply(lambda x: (x>0).sum()).reset_index(name = 'engagement_count')

st.dataframe(polls_melted)