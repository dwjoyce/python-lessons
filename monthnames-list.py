# monthnames-list.py
# Ask for a month number, and print out the name of the month.  This time use a list
# to store the names, and use the number as an index into the list.

month_names = ["January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December"]

month_str = input("Give me a month number: ")
month_num = int(month_str)

if month_num >= 1 and month_num <= 12:
    print("The name of the month is:", month_names[month_num - 1])
else:
    print("The number should be between 1 and 12!!!")
