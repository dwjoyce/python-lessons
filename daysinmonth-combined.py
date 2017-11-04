# daysinmonth-combined.py
# Ask user month number, and print out number of days in that month
# This time, we use logical operators to combine the output together and shorten the program

month_str = input("What is the month number? ")
month_num = int(month_str)

if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
    print("Month", month_num, "has 31 days")
elif month_num == 2:
    print("Month", month_num, "has 28 or 29 days")
elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
    print("Month", month_num, "has 30 days")
else:
    print("That month doesn't exist!")
