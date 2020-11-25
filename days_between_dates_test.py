import unittest
import datetime
import numpy as np
from days_between_dates import weekdays_between_dates

time1 = '2020-09-14 00:00:00+08:30'  # same local time in two different timezones
time2 = '2020-09-14 00:00:00+00:00'  # same local time in two different timezones
time3 = '2016-02-29 00:00:00+00:00'  # Leap year
time4 = '2017-11-23 13:00:50+00:00'  # random date with a time
weekday1 = '2020-11-23'  #Monday
weekday2 = '2020-11-22'  #Sunday
weekday3 = '2020-11-30'  #Next Monday
weekday4 = '2020-12-14'  #Three weeks
weekday5 = '2020-12-15'  #Three weeks + 1 day

class MyTestCase(unittest.TestCase):

    def test_weekdays(self):
        self.assertEqual(weekdays_between_dates(weekday2, weekday3)[1], np.busday_count(weekday2,weekday3))
        self.assertEqual(weekdays_between_dates(weekday2,weekday5)[1], np.busday_count(weekday2,weekday5))
        self.assertNotEqual(weekdays_between_dates(weekday2,weekday5,include_end_date=True)[1], np.busday_count(weekday2,weekday5))

    def no_difference(self):
        self.assertEqual(weekdays_between_dates(weekday2, weekday4)[2], 3)
        self.assertEqual(weekdays_between_dates(weekday1, weekday4, include_end_date=True)[2], 3)
        self.assertNotEquals(weekdays_between_dates(weekday1,weekday2)[2], 0)


if __name__ == '__main__':
    unittest.main()
