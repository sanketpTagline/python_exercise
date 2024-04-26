# import datetime as dt 
 

# Starting_date =  input(dt.datetime)
# print(Starting_date)

# Ending_date =   input(dt.datetime)
# print(Ending_date)

 
# 2024-04-26 11:41:56.977030
from datetime import datetime
date_format = "%d/%m/%Y"
# s1 = now.strftime("%m/%d/%Y, %H:%M:%S") 


staring_date=input("\nEnter Your Starting Date\n(Enter date as \"DD/MM/YYYY\")\n-> ")
Ending_date=input("\nEnter Your Ending Date\n(Enter date as \"DD/MM/YYYY\")\n-> ")

# today_date=datetime.today().strftime(date_format)
# today_date = datetime.strptime(today_date, date_format)

due_date = datetime.strptime(staring_date, date_format)
Ending_date = datetime.strptime(Ending_date, date_format)


x = abs(Ending_date-due_date)
if due_date<Ending_date:
    print(f"{x.days} Days Overdue")
elif due_date>Ending_date:
    print(f"{x.days} Days: Remaining")
else:
    print("Today is the last date")