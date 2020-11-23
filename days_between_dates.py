import datetime as dt

# Let's write the function to calculate the days between the dates. This function will take in ISO formatted datetime
# strings YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
def days_between_dates(date1,date2):
    date1 = dt.datetime.fromisoformat(date1)
    date2 = dt.datetime.fromisoformat(date2)
    timedelta = abs(date1-date2)
    return timedelta

def weekdays_between_dates(date1,date2):
    date1 = dt.datetime.fromisoformat(date1)
    date2 = dt.datetime.fromisoformat(date2)
    timedelta = abs(date1-date2)
    return timedelta