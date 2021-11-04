import datetime

counter = 0
year = 1901
month = 1

_day = datetime.date(year,month,1)

while(_day.year < 2001):
	if(_day.weekday() == 2):
		counter += 1
	if(month+1 == 13):
		month = 1
		year += 1
	else:
		month += 1
	_day = datetime.date(year,month,1)

print(counter)