import datetime

import pytz

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
localtime = datetime.datetime.now(tz=tz_to_display)
print(localtime)
print(datetime.datetime.utcnow())

for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(pytz.country_names[x])
