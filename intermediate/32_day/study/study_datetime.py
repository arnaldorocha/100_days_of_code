import datetime as dt

now = dt.datetime.now()
year = now.year
month= now.month
day_of_week = now.weekday()
print(day_of_week) # conta a partir do zero

date_of_birth = dt.datetime(year=1994 , month= 6, day= 15, hour= 16)
print(date_of_birth)

# if year == 2020:
#     print("Ano novo")
# else:
#     print("ano velho")


# print(now)

