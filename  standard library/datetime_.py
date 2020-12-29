import datetime
import sys


print("--------------- 1 -------------------")


## Exercise 1
## Using the built-in datetime module, create date objects for the given dates:
## EXPECTED RESULT: 2021-01-01 \ 31-7-21 \ May 7,1990

year_one =  datetime.date(2021,1,1)
year_two = datetime.date(2021,7,31)
year_string = datetime.date(1990,5,7)
print(year_one)
print(year_two.strftime("%d -%m -%y"))
print(year_string.strftime("%b %d,%Y"))

print("--------------- 2 -------------------")


## Exercise 2
# Using the built-in datetime module, create time objects for the given hours:
# EXPECTED RESULT: 12:00:00 \ 6:30:00 \  9:15:00

date_one =  datetime.time(12, 00, 00)
date_two =  datetime.time(6, 30, 00)
date_three = datetime.time(9,15,00)

print(date_one)
print(date_two)
print(date_three)

print("--------------- 3 -------------------")


## Exercise 3
# Using the built-in datetime module, create datetime objects for the given dates:
# EXPECTED RESULT: Jul 20 2020 11:30:00 \ 1990-03-10 12:00:00 \ 2021-01-01 00:00:00

date_time_one = datetime.datetime(2020,7,20,11,30,00)
date_time_two = datetime.datetime(1990,3,10,12,00,00)
date_time_three = datetime.datetime(2021,1,1,00,00,00)

print(date_time_one.strftime("%b %d %Y   %H:%M:%S"))
print(date_time_two.strftime("%Y-%m-%d   %H:%M:%S"))
print(date_time_three.strftime("%Y-%m-%d %H:%M:%S"))

print("--------------- 4 -------------------")


## Exercise 4
# Using the built-in datetime module, determine the number of days
## between 2020-07-21 and 2020-12-31
# EXPECTED RESULT: Number of days: 163

x =  datetime.date(2020,7,21)
y = datetime.date(2020,12,31)

calculate_days = (y -x).days
print(f"Number of days: {calculate_days}")

print("--------------- 5 -------------------")


## Exercise 5
# Using the built-in datetime module, determine the exact time elapsed between the dates:
# EXPECTED RESULT: 214 days, 22:55:00


x =  datetime.datetime(2020,7,20,11,30,00)
y =  datetime.datetime(2021,2,20,10,25,00)

calculate_days = (y-x)

print(f"{calculate_days}")

print("--------------- 6 -------------------")


## 6 Exercise
# Using the built-in datetime module and the strptime() function,parse the following str objects
# date_str_1 = '3 March 1995'
# date_str_2 = '3/9/1995'
# date_str_3 = '21-07-2021'
# EXPECTED RESULT: 1995-03-03 00:00:00 / 1995-09-03 00:00:00 / 2021-07-21 00:00:00

from datetime import datetime



date_str_on = '3 March 1995'
date_str_tw = '3/9/1995'
date_str_th = '21-07-2021'

dt1 =  datetime.strptime(date_str_on,'%d %B %Y')
dt2 =  datetime.strptime(date_str_tw,'%d/%m/%Y')
dt3 =  datetime.strptime(date_str_th,'%d-%m-%Y')

print(dt1)
print(dt2)
print(dt3)

print("--------------- 7 -------------------")


## 7 Using the built-in datetime module, determine the number of days until
## the end of the current year



from datetime import date
import datetime


now  = date.today()
endDay = datetime.date(2020,12,31)
lDay = (endDay-now).days
print(f"Number of days until the end of the year: {lDay} ")


print("--------------- 8 -------------------")

# Using the built-in datetime module, determine the exact time remaining until the
# end of the current year


import datetime

dtn = datetime.datetime.now()
end = datetime.datetime(now.year + 1,1,1)
dif = end - dtn
print(f"Until the end of the year: {dif}")

print("--------------- 9 -------------------")

# Using built-in datetime module, the date and timedelta classes from the given date 2020-01-01
# date 2020-01-01 00:00:00 get the date:

from datetime import datetime, timedelta

init = datetime.now()
future_seven_days = init + \
                    timedelta(days = 7)

future_thirty_days = init + \
                     timedelta(days = 30)

future_thirty_hours = init + \
                      timedelta(hours= 30)
future_thirty_minutes = init + \
                        timedelta(minutes= 15)

print("Initial date:", str(init))
print("Seven days:", str(future_seven_days))
print("Thirty days:", str(future_thirty_days))
print("Thirty hours:",str(future_thirty_hours))
print("Thirty minutes:",str(future_thirty_minutes))


print("--------------- 10 -------------------")

# Using the built-in datetime module calculate the future value of the investment(present value)
# of USD 1000 with an annual interest rate of 4% (rate) and daily compound capitalization of
# interest, assuming the duration of the investment from 2021-07-01 to 2021-12-31
# For calculations,assume that the year has 365 days.
# EXPECTED RESULT: future value: 1020.26

import datetime



present_value = 1000
rate = 0.04
star = datetime.date(2021,7,1)
end  = datetime.date(2021,12,31)
dif = (end - star).days
daily = rate / 365
future_value = present_value*(1 + daily)**dif
print(f"Future value: {future_value:.2f}")
