# #  Date and Time
import datetime
a=datetime.datetime.now()
#
# print(a) # To Get current date and time
#
# print(a.strftime("%A")) # full version	Wednesday
#
# print(a.strftime("%a")) # short version	Wed
#
# print(a.strftime("%B")) # Month name, full version	December
#
# print(a.strftime("%b")) # Month name, short version	Dec
#
print(a.strftime("%c")) # Local version of date and time	Mon Dec 31 17:41:00 2018
#
# print(a.strftime("%d")) # Day of month 01-31	31
#
# print(a.strftime("%f")) # Microsecond 000000-999999	548513
#
# print(a.strftime("%H")) # Hour 00-23	17
#
# print(a.strftime("%I")) # Hour 00-12	05
#
# print(a.strftime("%j")) # Day number of year 001-366	365
#
# print(a.strftime("%M")) # Minute 00-59	41
#
# print(a.strftime("%m")) # Month as a number 01-12	12
#
# print(a.strftime("%p")) # AM/PM	PM
#
# print(a.strftime("%S")) # Second 00-59	08
#
# print(a.strftime("%U")) # Week number of year, Sunday as the first day of week, 00-53	52
#
# print(a.strftime("%W")) # Week number of year, Monday as the first day of week, 00-53	52
#
# print(a.strftime("%w")) # Weekday as a number 0-6, 0 is Sunday	3
#
# print(a.strftime("%X")) # Local version of time	17:41:00
#
# print(a.strftime("%x")) # Local version of date	12/31/18
#
# print(a.strftime("%Y")) # Year, full version	2018
#
# print(a.strftime("%y")) # Year, short version, without century	18

print(a.strftime("%Z")) # Timezone	CST

print(a.strftime("%z")) # UTC offset	+0100

# import time;
#
# # prints the number of ticks spent since 12 AM, 1st January 1970
#
# print(time.time())