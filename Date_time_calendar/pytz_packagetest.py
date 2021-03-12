import pytz
import datetime

country = "Africa/Lagos"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, local_time))
print("The UTC time is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]))

# for i in sorted(pytz.country_names):
#     print("{}: {}: {}".format(i, pytz.country_names[i], pytz.country_timezones.get(i)))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zones in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zones)
            print("\t\t{}: {}".format(zones, datetime.datetime.now(tz=tz_to_display)))
    else:
        print("\t\tNo timezone is defined")
