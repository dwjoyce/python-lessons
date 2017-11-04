# daysinmonth-list.py
# Ask user month number, and print out number of days in that month
# This time, we use lists to store which month has what number of days

MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]  # Jan, Mar, May, Jul, Aug, Oct and Dec have 31 days
MONTHS_WITH_30_DAYS = [4, 6, 9, 11]            # Apr, Jun, Sept and Nov have 30 days

month_str = input("What is the month number? ")
month = int(month_str)

if month in MONTHS_WITH_31_DAYS:
    print("Month", month, "has 31 days")
elif month in MONTHS_WITH_30_DAYS:
    print("Month", month, "has 30 days")
elif month == 2:
    print("Month", month, "has 28 or 29 days")
else:
    print("That month doesn't exist!")
