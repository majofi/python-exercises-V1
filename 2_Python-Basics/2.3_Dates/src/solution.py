# 2.3.1.1

import time
import datetime
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))

# 2.3.1.2
print(calendar.isleap(2021))

# 2.3.1.3
from datetime import datetime
date_object = datetime.strptime('Jul 1 2014 3:00PM', '%b %d %Y %I:%M%p')
print(date_object)

# 2.3.1.4
import datetime
print(datetime.datetime.now().time())

# 2.3.1.5
import datetime
print(
    datetime.datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

# 2.3.1.6

import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)

# 2.3.1.7

from datetime import date
from datetime import timedelta
today = date.today()
offset = (today.weekday() - 1) % 7
last_tuesday = today - timedelta(days=offset)
print(last_tuesday)
