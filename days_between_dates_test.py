import unittest
import datetime
from days_between_dates import days_between_dates

time1 = '2020-09-14 00:00:00+08:30'  # same local time in two different timezones
time2 = '2020-09-14 00:00:00+00:00'  # same local time in two different timezones
time3 = '2016-02-29 00:00:00+00:00'  # Leap year
time4 = '2017-11-23 13:00:50+00:00'  # random date with a time


class MyTestCase(unittest.TestCase):

    def test_timezones(self):
        self.assertEqual(days_between_dates(time1, time2), datetime.timedelta(seconds=30600))

    def no_difference(self):
        self.assertEqual(days_between_dates(time1, time2), datetime.timedelta(seconds=0))


if __name__ == '__main__':
    unittest.main()
