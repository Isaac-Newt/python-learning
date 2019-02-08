#
# Isaac List - CS150 - October 3, 2018 - Lab 5
# 
# This program implements Zeller's Congruence 
# for all months.
#


def inputInt(prompt) :

    value = input(prompt + '(an int) ')
    value = int(value)

    return value


def zellerValue(month, day, year) :
    
    # If month == 1 or 2, pretend date is month 13 or 14 
    # of previous year (i.e. 2/24/2018 --> 14/24/2017)
    if month == 1 or month == 2:
        month = month + 12
        year = year - 1
    
    # Some Fun Math :)
    month = month - 2
    a = (month * 26 - 2) // 10
    b = year % 100
    c = year // 100
    d = b // 4
    e = c // 4
    f = day + a + b + 5 * c + d + e
    dayOfWeek = f % 7
    
    # dayOfWeek: 0-6 --> Sunday-Saturday 
    if dayOfWeek == 0:
        dayOfWeek = "Sunday"
    elif dayOfWeek == 1:
        dayOfWeek = "Monday"
    elif dayOfWeek == 2:
        dayOfWeek = "Tuesday"
    elif dayOfWeek == 3:
        dayOfWeek = "Wednesday"
    elif dayOfWeek == 4:
        dayOfWeek = "Thursday"
    elif dayOfWeek == 5:
        dayOfWeek = "Friday"
    else:
        dayOfWeek = "Saturday"
    
    return dayOfWeek


month = inputInt('Enter a month in the range 1-12: ')
day = inputInt('Enter a day-of-month in the range 1-31: ')
year = inputInt('Enter a year: ')

print( \
    'The date', \
    str(month) + '-' + str(day) + '-' + str(year), \
    'occurs on day', \
    zellerValue(month, day, year) \
    )
