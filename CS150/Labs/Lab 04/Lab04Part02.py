# Isaac List - CS150 - September 24, 2018
# 
# This program implements Zeller's Congruence, but only for
# dates in the months March-December

# Useful function
def inputInt(prompt) :
    value = input(prompt + '(an int) ')
    value = int(value)

    return value

# Do calculations
def dayOfWeekFinder(month, day, year):
    month = month - 2
    a = (month * 26 - 2) // 10
    b = year % 100
    c = year // 100
    d = b // 4
    e = c // 4
    f = day + a + b + 5 * c + d + e
    dayOfWeek = f % 7   
    
    return dayOfWeek

# Get Inputs
month = inputInt('Enter a month in the range 3-12: ')
day = inputInt('Enter a day-of-month in the range 1-31: ')
year = inputInt('Enter a year: ')

# Define dayOfWeek
dayOfWeek = dayOfWeekFinder(month, day, year)

# Provide a response
print('The date', str(month) + '-' + str(day) + '-' + str(year), 'occurs on day', dayOfWeek)
