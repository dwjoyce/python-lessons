# date.py
# Ask for the current date in the format DD/MM/YY, and print out in a more readable form

months = "January February March April May June July August September October November December"
month_names = months.split()

date = input("What is today's date, in the format DD/MM/YY? ")

d, m, y = date.split("/")
m = int(m)

if d >= "11" and d <= "19":
    postfix = "th"
elif d.endswith("1"):
    postfix = "st"
elif d.endswith("3"):
    postfix = "rd"
elif d.endswith("2"):
    postfix = "nd"
else:
    postfix = "th"

print("Today's date is", d + postfix, "of", month_names[m - 1], y)
