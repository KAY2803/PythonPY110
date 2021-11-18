#скрипт для извлечения года, месяца, даты и времени с помощью Lambda

import datetime

dt = datetime.datetime.now()
year = lambda x: str(dt)[:4]
month = lambda x: str(dt)[5:7]
day = lambda x: str(dt)[8:10]
time = lambda x: str(dt)[11:]

print(dt)
print(f'год: {year(dt)}, месяц {month(dt)}, дата {day(dt)}, время {time(dt)}')
