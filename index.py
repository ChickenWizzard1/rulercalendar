"""var days_since_epoch = (now.getTime() - epoch.getTime() ) / day_length_milliseconds

            rc_years = days_since_epoch / 30.4375
            rc_years_floor = Math.floor(rc_years)

            rc_months = (rc_years - rc_years_floor) * 12
            rc_months_floor = Math.floor(rc_months)

            rc_days = (rc_months - rc_months_floor) * 30.4375
            rc_days_floor = Math.floor(rc_days)

            rc_hours = (rc_days - rc_days_floor) * 24
            rc_hours_floor = Math.floor(rc_hours)

            rc_minutes = (rc_hours - rc_hours_floor) * 60
            rc_minutes_floor = Math.floor(rc_minutes)

            rc_seconds = (rc_minutes - rc_minutes_floor) * 60
            rc_seconds_floor = Math.floor(rc_seconds)
import math
import datetime
from datetime import timedelta
day_length_milliseconds = 24 * 60 * 60 * 1000
now = datetime.datetime.today()
epoch = datetime.datetime(2022, 1, 1, 0, 0, 0)
d = (now - epoch)
 #just for me so I can see what d is a lot easier.
print("d is:")
print(d)
print(now)
days_since_epoch= d / day_length_milliseconds
print (day_length_milliseconds)
print(days_since_epoch)
rc_years = days_since_epoch / 30.4375
print(rc_years)"""
#import pandas as pd

import datetime
import math
def time_to_int(dateobj):
    total = int(dateobj.strftime('%S'))
    total += int(dateobj.strftime('%M')) * 60
    total += int(dateobj.strftime('%H')) * 60 * 60
    total += (int(dateobj.strftime('%j')) - 1) * 60 * 60 * 24
    total += (int(dateobj.strftime('%Y')) - 1970) * 60 * 60 * 24 * 365
    return total

today = datetime.date.today()
d1 = datetime.date(year=2022, month=1, day=1)
d1 = time_to_int(d1)
today  = time_to_int(today)
d2 =  today-d1

day_length_milliseconds = 24 * 60 * 60 * 1000
days_since_epoch = d2 / day_length_milliseconds
# * 1000 so it would be (to example) 180.0 days instead of 0.180
days_since_epoch = days_since_epoch * 1000

print(days_since_epoch)
rc_years = days_since_epoch / 30.4375
rc_years_floor = math.floor(rc_years)
rc_months = (rc_years - rc_years_floor) * 12
rc_months_floor = math.floor(rc_months)
print(rc_years, rc_months)
print(rc_years_floor, rc_months_floor)
