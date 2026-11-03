import datetime

mikes_dob = 'Dec 6, 1970'
mikes_dob_date = datetime.datetime.strptime(mikes_dob, '%b %d, %Y').date()
four_weeks = datetime.timedelta(days = 28)
four_weeks_from_dob = mikes_dob_date + four_weeks
mike_dob_dow = datetime.datetime.strftime(mikes_dob_date, '%A')

today = datetime.date.today()