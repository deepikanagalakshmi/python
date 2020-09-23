import calendar

print(calendar.firstweekday());
print()

print(calendar.month(2020,10))
print()

print(calendar.weekheader(3))
print()

print(calendar.monthcalendar(2020,11))
print()

print(calendar.calendar(2020))
print()

day_of_the_week=calendar.weekday(2020,9,23)
print(day_of_the_week)
print()

is_leap_year=calendar.isleap(2020)
print(is_leap_year)
print()

how_many_leap_days=calendar.leapdays(2020,2030)
print(how_many_leap_days)
