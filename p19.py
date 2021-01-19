#
#
# You are given the following information, but you may prefer to do some research for yourself.
#
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


import datetime

start = datetime.datetime.now()
print(start)

# 1 = monday, 2 = tuesday... 7 = sunday
days_of_week = [1, 2, 3, 4, 5, 6, 7]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False


sunday_count = 0
day_counter = 0
for year in range(1901, 2001):

    for month in range(len(days_in_month)):

        if days_in_month[month] == 28 and is_leap_year(year):
            # print(f"{year} leapyear")
            num_days = 29
        else:
            num_days = days_in_month[month]

        for day in range(num_days):
            dow = days_of_week[(day_counter % 7) - 1]
            # print(f"year: {year} - month(0based): {month} - num days: {num_days} - day(0based): {day} - DOW: {dow}")
            if day == 0 and dow == 7:  # Sunday
                sunday_count += 1
            day_counter += 1


print(f"sunday_count: {sunday_count}")

print(f"FINISHED")
end = datetime.datetime.now() - start
print(end)
