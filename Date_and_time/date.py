import time
print(time.localtime(time.time())) # to get the detailed current time


# to get the formatted time

import time

print(time.asctime(time.localtime(time.time()))) #The time can be formatted by using the asctime() function of time module


# sleep ()

import time
for i in range(0,5):
    print(i)
    #Each element will be printed after 1 second
    time.sleep(2)

# returns the current datetime object
import datetime

print(datetime.datetime.now())

# returns the datetime object for the specified time

import datetime
print(datetime.datetime(2018, 12, 10, 14, 15, 10))

#  returns the datetime object for the specified date
import datetime
print(datetime.datetime(2018, 12, 10))
