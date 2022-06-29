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
from datetime import timedelta
day_length_milliseconds = 24 * 60 * 60 * 1000
now = datetime.datetime.now()
epoch = [2022, 1, 1, 0, 0, 0,]
 #days_since_epoch = now - epoch
#definine time in this moment.
now = [now.year, now.day, now.month, now.hour, now.minute, now.second]
print (day_length_milliseconds)
# subtract daytime (not done)  
d = datetime.datetime.today() - timedelta(days=2)
#just for me so I can see what d is a lot easier.
print("d is:")
print(d)
print(now)
