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
            rc_seconds_floor = Math.floor(rc_seconds)"""

import datetime
import math
import time_module
from time_module import time_to_int

today = datetime.date.today()
d1 = datetime.date(year=2022, month=1, day=1)
d1 = time_to_int(d1)
today  = time_to_int(today)
d2 =  today-d1

day_length_milliseconds = 24 * 60 * 60 * 1000
days_since_epoch = d2 / day_length_milliseconds
days_since_epoch = days_since_epoch * 1000

print(days_since_epoch)
rc_years = days_since_epoch / 30.4375
rc_years_floor = math.floor(rc_years)
rc_months = (rc_years - rc_years_floor) * 12
rc_months_floor = math.floor(rc_months)
print(rc_years, rc_months)
print(rc_years_floor, rc_months_floor)
