import datetime as dt


# Let's write the function to calculate the days between the dates. This function will take in ISO formatted datetime
# strings YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
def days_between_dates(date1, date2):
    date1 = dt.datetime.fromisoformat(date1)
    date2 = dt.datetime.fromisoformat(date2)
    timedelta = abs(date1 - date2)
    return timedelta.days


def time_between_dates(date1, date2, include_end_date=False, time_units='days', report_units='days'):
    try:
        date1 = dt.datetime.fromisoformat(date1)
        date2 = dt.datetime.fromisoformat(date2)
    except:
        return 'Input Error. Please format date strings as YYYY-MM-DD'
    else:
        # Make the weekday mask, this will add some extensibility if we need to define weekends differently
        # for an upcoming 4 day work week at some point
        weekdays_mask = [0, 1, 2, 3, 4]  # 5 and 6 correspond to saturday and sunday
        # Work out start and end date in case user has called API in wrong order
        if date1 > date2:
            start, end = date2, date1
        else:
            start, end = date1, date2
        if include_end_date:
            end = end + dt.timedelta(days=1)
        timedelta = end-start
        total_days = timedelta.days
        # Initialise a dictionary to track number of each weekday
        weekday_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        total_weeks = total_days // 7
        remainder_days = total_days % 7
        start_day = start.weekday()
        # Need to create array for remaining weekdays and rotate it to line up to start day
        extra_days = [1 if i < remainder_days else 0 for i in range(7)]
        extra_days = extra_days[-start_day:] + extra_days[:-start_day]
        for day, extra_day in zip(weekday_count, extra_days):
            weekday_count[day] += total_weeks + extra_day
        # Now just sum up days that match the mask and return total value
        total_weekdays = 0
        for weekday in weekdays_mask:
            total_weekdays += weekday_count[weekday]
        # Turn the results into a timedelta
        total_days = dt.timedelta(days=total_days)
        total_weeks = dt.timedelta(days=total_weeks*7)
        total_weekdays = dt.timedelta(days=total_weekdays)
        # Call the function to change the units to what we want
        return time_report_units(total_days, report_units),\
               time_report_units(total_weekdays, report_units), \
               time_report_units(total_weeks, report_units)

def time_report_units(timedelta, units='days'):
    if units == 'seconds':
        return timedelta.total_seconds()
    elif units == 'minutes':
        return timedelta.total_seconds()//60
    elif units == 'hours':
        return timedelta.total_seconds()//3600
    elif units =='days':
        return timedelta.days
    elif units == 'years':
        return timedelta.total_seconds()/31536000