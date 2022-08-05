from datetime import datetime, timedelta

date_ = input()
new_days = int(input())
datetimeString = datetime.strptime(date_,'%Y %m %d') + timedelta(days=new_days)
print(datetimeString.year, datetimeString.month, datetimeString.day)