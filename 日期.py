year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    days = months[month - 1]
else:
    print('data error')
days += day

leap = 0
if (year % 4 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month == 2):
    days += leap
print('it is the {}th day.'.format(days,))
