import calendar



print(range(1, calendar.monthrange(2019, 11)[1]))

for i in range(1, calendar.monthrange(2019, 11)[1] + 1):
    print(i)