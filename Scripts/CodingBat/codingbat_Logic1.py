# Cigar Party
def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  elif is_weekend:
    if cigars >= 40:
      return True
    else:
      return False
  elif cigars >= 61:
    return False
  elif cigars >= 40:
    return True

# Date Fasion
def date_fashion(you, date):
  if you <= 2 or date <=2:
    return 0
  elif you >= 8 or date >=8:
    return 2
  else:
    return 1

# Squirrel Play
def squirrel_play(temp, is_summer):
  if is_summer == True:
    if temp >= 60 and temp <= 100:
      return True
    else:
      return False
  else:
    if temp >= 60 and temp <= 90:
      return True
    else:
      return False

# Caught Speeding
def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed <= 65:
      return 0
    elif speed >= 86:
      return 2
    else:
      return 1
  else:
    if speed <= 60:
      return 0
    elif speed >= 81:
      return 2
    else:
      return 1

# Sorta Sum
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  else:
    return a + b

# Alarm Clock
def alarm_clock(day, vacation):
  if vacation == True:
    if day == 0 or day == 6:
      return "off"
    else:
      return "10:00"
  else:
    if day == 0 or day == 6:
      return "10:00"
    else:
      return "7:00"

# Love 6
def love6(a, b):
  if a == 6 or b == 6:
    return True
  elif (a + b == 6) or (abs(a - b) == 6):
    return True
  else:
    return False

# In 1 to 10
def in1to10(n, outside_mode):
  if outside_mode == True:
    if n <= 1 or n >= 10:
      return True
    else:
      return False
  else:
    if n >= 1 and n <= 10:
      return True
    else:
      return False

# Near 10
def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True
  else:
    return False