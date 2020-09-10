import calendar

ay,gun,il = map(int, input().split())
print(calendar.day_name[calendar.weekday(il, ay, gun)].upper())
