# daysinmonth.py
# Ask for month number, and print out how many days are in that month

month_num_str = input("What is the month number? ")
month_num = int(month_num_str)

if month_num == 1:
    print("31 days")
elif month_num == 2:
    print("28 or 29 days")
elif month_num == 3:
    print("31 days")
elif month_num == 4:
    print("30 days")
elif month_num == 5:
    print("31 days")
elif month_num == 6:
    print("30 days")
elif month_num == 7:
    print("31 days")
elif month_num == 8:
    print("31 days")
elif month_num == 9:
    print("30 days")
elif month_num == 10:
    print("31 days")
elif month_num == 11:
    print("30 days")
elif month_num == 12:
    print("31 days")
else:
    print("No such month number!")
