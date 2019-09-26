# Adds "not" to a string
def not_string(str):
  # Gets first 3 characters in string
  if (str[:3] == "not"):
    return str
  else:
    return "not " + str
    
# Remove the nth letter in string
def missing_char(str, n):
  new_string = str[:n] + str[n+1:]
  return new_string

# Switch first and last letters in string
def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str)-1] + str[1:-1] + str[0]

# Print first three chars in string 3 times
def front3(str):
  three = str[0:3]
  return three + three + three
