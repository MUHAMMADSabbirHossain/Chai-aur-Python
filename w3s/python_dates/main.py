import datetime

print(f"Pythone Dates")

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

print(x.strftime("%A"))
print(x.strftime("%B"))

y = datetime.datetime(2020, 5, 17)
print(y)