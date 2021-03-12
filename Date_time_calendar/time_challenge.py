import datetime
import pytz

# print("monotonic(): {}".format(time.get_clock_info("monotonic")))
# print("perf_counter(): {}".format(time.get_clock_info("perf_counter")))
# print("time(): {}".format(time.get_clock_info("time")))
# print("process_time(): {}".format(time.get_clock_info("process_time")))
# print(pytz.all_timezones)

timezone_list = ["Africa/Accra",
                 "Africa/Bissau",
                 "Asia/Beirut",
                 "Asia/Chita",
                 "Atlantic/Bermuda",
                 "Canada/Pacific",
                 "America/Yellowknife",
                 "America/Panama",
                 "Europe/Andorra",
                 ]

for index, zone in enumerate(timezone_list):
    print("{}: {}".format(index + 1, zone))

while True:
    users_input = int(input("Choose a timezone from the list above: "))
    if users_input == 0:
        break
    if users_input in range(1, 10):
        tz_to_display = pytz.timezone(timezone_list[users_input - 1])
        local_time = datetime.datetime.now(tz=tz_to_display)
        print("Local time is {}".format(datetime.datetime.now().strftime("%A %x %X %z")))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime("%A %x %X %z")))

        print("The time in {} is {}, time zone is {}"
              .format(timezone_list[users_input - 1], local_time.strftime("%A %x %X %z"), local_time.tzinfo))
        print()
