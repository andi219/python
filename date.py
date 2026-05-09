import datetime
#year.month.day.hour.minute.secon.microsecon
x=datetime.datetime.now()
print(x)
#print only year
print(x.year)
print(x.strftime("%Y"))
#costume date time
c = datetime.datetime(1999, 8, 12)
print(c)