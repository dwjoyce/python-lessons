#!/usr/bin/env python
# encoding: utf-8

# birthday.py
# Input birthday date, and calculate number of days from today to that date.

import sys
import datetime

MONTHS_WITH_31_DAYS = (1, 3, 5, 7, 8, 10, 12)  # Jan, Mar, May, Jul, Aug, Oct and Dec have 31 days
MONTHS_WITH_30_DAYS = (4, 6, 9, 11)            # Apr, Jun, Sept and Nov have 30 days

def leap_year(year):
    """Return true if supplied year is a leap year."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month, year):
    """Returns the number of days in the supplied month, and year,
    taking leap years into account."""
    if month in MONTHS_WITH_31_DAYS:
        days = 31
    elif month in MONTHS_WITH_30_DAYS:
        days = 30
    elif month == 2:
        if leap_year(year):
            days = 29
        else:
            days = 28
    else:
        days = 0
    return days

def days_in_year(year):
    """Returns the number of days in a year, depending on whether the
    year is a leap year or not."""
    if leap_year(year):
        return 366
    return 365

def valid_date(day, month, year):
    """Returns True if the supplied date is valid, False otherwise."""
    return ((day > 0) and
            (day <= days_in_month(month, year)) and
            (month > 0) and
            (month <= 12))

def days_till_birthday(birthday_day, birthday_month):
    """Returns the numbers of days from today"s date to the birthday date supplied."""
    
    # Get today"s date
    today = datetime.date.today()
    day1 = today.day
    month1 = today.month
    year1 = today.year
    
    day2 = birthday_day
    month2 = birthday_month

    # Initialise year2 to present year for starters.
    year2 = today.year

    # Increment month / year if user has already had birthday this year
    if month1 > month2:
        year2 += 1
    elif (day1 > day2) and (month1 == month2):
        year2 += 1

    # If birthday is on the last day of Feburary, then increment year until a leap year is found
    if month2 == 2 and day2 == 29:
        while not leap_year(year2):
            year2 += 1

    # Test date is valid first
    if not valid_date(day2, month2, year2):
        return None

    totalDays = 0

    # Count up until the days are the same
    while day1 != day2:
        totalDays += 1
        day1 += 1
        if day1 > days_in_month(month1, year1):
            day1 = 1
            month1 += 1
      
        if month1 > 12:
            month1 = 1
            year1 += 1

    # Count up until the months are the same
    while month1 != month2:
        totalDays += days_in_month(month1, year1)
        month1 += 1
        if month1 > 12:
            month1 = 1
            year1 += 1

    # Count up until the years are the same
    while year1 != year2:
        totalDays += days_in_year(year1)
        year1 += 1
        
    return totalDays

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # Get birthday from command line
        birthday_date = sys.argv[1]
    else:
        # Ask for the user's birthday
        birthday_date = input("Enter your birthday (in the format dd/mm): ")
    date_split = birthday_date.split("/")

    # Separate into day and month
    day, month = int(date_split[0]), int(date_split[1])

    # Get total number of days till user"s birthday
    totalDays = days_till_birthday(day, month)

    if totalDays != None:  # valid result
        print("Total number of days till your birthday is", totalDays)
        if totalDays == 0:
            print("HAPPY BIRTHDAY!!!")
