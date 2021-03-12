import time
import random

print(time.gmtime(0))   # to check the epoch time
print(time.localtime())

# accessing the struct_time with a named tuple interface
new_time = time.localtime()
print("Year: {}, Month: {}, Day: {}"
      .format(new_time.tm_year, new_time.tm_mon, new_time.tm_mday))

print("Year: {}, Month: {}, Day: {}"
      .format(new_time[0], new_time[1], new_time[2]))

print("*" * 50)
input("Press ENTER to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = time.perf_counter()

input("Press ENTER to stop")
end_time = time.perf_counter()

print("Started at {}"
      .format(time.strftime("%X", time.localtime(start_time))))
print("Ended at {}"
      .format(time.strftime("%X", time.localtime(end_time))))

print("Total reaction time is {} seconds".format(end_time - start_time))
