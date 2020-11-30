import unittest
import numpy as np
from api_date_functions import *

time1 = '2020-09-14 00:00:00+08:30'  # same local time in two different timezones
time2 = '2020-09-14 00:00:00+00:00'  # same local time in two different timezones
time3 = '2016-02-29 00:00:00+00:00'  # Leap year
time4 = '2017-11-23 13:00:50+00:00'  # random date with a time
time5 = '2015-11-23 13:00:50+00:00'  # 2 years from time 4
time6 = '2014-11-23 13:00:50+00:00'  # 1 year from time 5
weekday1 = '2020-11-23'  # Monday
weekday2 = '2020-11-22'  # Sunday
weekday3 = '2020-11-30'  # Next Monday
weekday4 = '2020-12-14'  # Three weeks
weekday5 = '2020-12-15'  # Three weeks + 1 day
bad_date_string_error = 'Input Error. Please format date strings as YYYY-MM-DD'


class InputValidation(unittest.TestCase):

    def test_order_of_dates(self):
        self.assertEqual(time_between_dates(weekday1, weekday2), time_between_dates(weekday2, weekday1))
        self.assertEqual(time_between_dates(weekday3, weekday4), time_between_dates(weekday4, weekday3))

    def test_bad_string(self):
        self.assertEqual(time_between_dates('bad-string', weekday3), bad_date_string_error)

    def test_weekdays(self):
        self.assertEqual(time_between_dates(weekday2, weekday3)[1], np.busday_count(weekday2, weekday3))
        self.assertEqual(time_between_dates(weekday2, weekday5)[1], np.busday_count(weekday2, weekday5))
        self.assertNotEqual(time_between_dates(weekday2, weekday5, include_end_date=True)[1],
                            np.busday_count(weekday2, weekday5))

    def no_difference(self):
        self.assertEqual(time_between_dates(weekday2, weekday4)[2], 3)
        self.assertEqual(time_between_dates(weekday1, weekday4, include_end_date=True)[2], 3)
        self.assertNotEquals(time_between_dates(weekday1, weekday2)[2], 0)


class ReportUnitValidation(unittest.TestCase):

    def test_seconds(self):
        self.assertEqual(time_between_dates(weekday1, weekday2, report_units='seconds')[0], 86400)

    def test_minutes(self):
        self.assertEqual(time_between_dates(weekday1, weekday2, report_units='minutes')[0], 1440)

    def test_hours(self):
        self.assertEqual(time_between_dates(weekday1, weekday2, report_units='hours')[0], 24)

    def test_days(self):
        self.assertEqual(time_between_dates(weekday1, weekday2, report_units='days')[0], 1)

    def test_leap_years(self):
        self.assertEqual(time_between_dates(time4, time5, report_units='years')[0], 2)

    def test_years(self):
        self.assertEqual(time_between_dates(time6, time5, report_units='years')[0], 1)


class DateStringProcessing(unittest.TestCase):

    def test_bad_string(self):
        self.assertEqual(date_string_processor('bad-string'), 0)

    def test_good_string(self):
        self.assertEqual(date_string_processor(weekday2), None)

    def test_null_string(self):
        self.assertIsNone(date_string_processor(None), None)

    def test_extreme_string(self):
        self.assertEqual(date_string_processor('1969-01-01'), 0)


if __name__ == '__main__':
    unittest.main()
