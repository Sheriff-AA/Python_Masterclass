import time
import datetime

print("The epoch time starts at {}".format(time.strftime("%c", time.gmtime(0))))

print(time.tzname)
print(time.timezone)

print("The current time zone is {}, with an offset of {}"
      .format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight saving is in effect for this location")
    print("\tThe DST timezone is {}".format(time.tzname[1]))

print("The local time is {}"
      .format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

print("The UTC time is {}"
      .format(time.strftime("%Y-%m-%d %H:%m:%S", time.gmtime())))

print("*" * 50)
print()
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
