months= {"JANUARY": 31,
    "FEBRUARY": 28,
    "MARCH": 31,
    "APRIL": 30,
    "MAY": 31,
    "JUNE": 30,
    "JULY": 31,
    "AUGUST": 31,
    "SEPTEMBER": 30,
    "OCTOBER": 31,
    "NOVEMBER": 30,
    "DECECMBER": 31}
month= input("month: ").upper()
days=0
days = months.get(month,days)
if month == "FEBRUARY":
    print("28 or 29 days")
elif days==0:
   print("Nhap lai !")
else:
    print(days, "days")