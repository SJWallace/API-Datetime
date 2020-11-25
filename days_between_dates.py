import datetime as dt

# Let's write the function to calculate the days between the dates. This function will take in ISO formatted datetime
# strings YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
def days_between_dates(date1,date2):
    date1 = dt.datetime.fromisoformat(date1)
    date2 = dt.datetime.fromisoformat(date2)
    timedelta = abs(date1-date2)
    return timedelta.days

def weekdays_between_dates(date1,date2):
    date1 = dt.datetime.fromisoformat(date1)
    date2 = dt.datetime.fromisoformat(date2)
    # Find out what days the start and end date are
    start_day = date1.weekday()
    # Make the weekday mask, this will add some extensibility if we need to define weekends differently
    # for an upcoming 4 day work week at some point
    weekdays_mask = [0, 1, 2, 3, 4]  #5 and 6 correspond to saturday and sunday
    timedelta = abs(date1-date2)
    total_days = timedelta.days
    # Initialise a dictionary to track number of each weekday
    weekday_count = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
    total_weeks = total_days // 7
    remainder_days = total_days % 7
    # Need to create array for remaining weekdays and rotate it to line up to start day
    extra_days = [1 if i < remainder_days else 0 for i in range(7)]
    extra_days = extra_days[start_day:] + extra_days[:start_day]
    for day, extra_day in zip(weekday_count,extra_days):
        weekday_count[day] += total_weeks + extra_day
    # Now just sum up days that match the mask and return total value
    total_weekdays = 0
    for weekday in weekdays_mask:
        total_weekdays += weekday_count[weekday]
    return total_days, total_weekdays, total_weeks