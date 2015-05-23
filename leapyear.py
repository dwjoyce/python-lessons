# leapyear.py
# Ask the user for a year, and tell the user whether it is a leap year or not

# Get a year from the user via a call to raw_input(), and then convert it
# straight away into an integer
year = int( raw_input( 'Please input year: ' ) )

# Set boolean "leap_year" to True if it is a leap year, otherwise False
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False
    
# This could be turned into one line with the following:
#leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if leap_year:
    print 'The year', year, 'is a leap year.'
else:
    print 'The year', year, 'is not a leap year.'
