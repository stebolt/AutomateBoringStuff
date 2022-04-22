# dateDetection.py
import re

thirtyDayMonths = {4, 6, 9, 11}
isLeapYear = False

dateRegex = re.compile(r'([0-3]\d)/([0-1]\d)/([1-2]\d{3})')
moDate = dateRegex.search('Todays date is 31/07/2022 - have a nice day!')
def validDateCheck(day, month, year, isLeapYear):
    if year % 4 == 0:               # Year divides by 4 is a leap year...
        isLeapYear = True
        if year % 100 == 0:         # ...Except for years divisibly by 100....
            isLeapYear = False
            if year % 400 == 0:     # Unless the year also divides by 400.
                isLeapYear = True
    if (month < 1 or month > 12 or day < 1 or day > 31):
        return False
    if month == 2:
        if day > 29:
            return False
        if not isLeapYear and day > 28:
            return False
    if month in thirtyDayMonths and day > 30:
        return False
    return True

if validDateCheck(int(day), int(month), int(year), isLeapYear):
    print('Valid date!')