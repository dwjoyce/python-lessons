# leapyear.py
# Program to ask for a year, and tell user whether it is a leap year or not.

# The rules are:
#  - if divisible by 400, then print out 'leap year'
#  - else if divisible by 100, then print out 'not leap year'
#  - else if divisible by 4, then print out 'leap year'
#  - else print out 'not leap year'

year = input('What year? ')
year = int(year)

if year % 400 == 0:
    print("That's a leap year!")
elif year % 100 == 0:
    print("That's not a leap year!")
elif year % 4 == 0:
    print("That's a leap year!")
else:
    print("That's not a leap year!")

# or you can test for leap year in one line as follows:
# ((year % 400) == 0) or (year % 4 == 0 and year % 100 != 0)
