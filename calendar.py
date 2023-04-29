#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar

month,date,year = map(int, input().split())
day_num = calendar.weekday(year, month, date)
print(calendar.day_name[day_num].upper())
