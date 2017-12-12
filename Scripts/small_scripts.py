phrase = "A bird in the hand..."

# Replace all A's in phrase with X
for char in phrase:
  if char == "A" or char == "a":
    print("X"),
  else:
    print(char),

print()

# # # # # # # # # #

numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
  print(num)

for num in numbers:
  print(num ** 2)
  
# # # # # # # # # #

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print(a)
  elif b > a:
    print(b)
    
# # # # # # # # # #

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
# # # # # # # # # #

def is_int(x):
  if x % 1 == 0:
    return True
  else:
    return False
  
# # # # # # # # # #

def digit_sum(n):
  string = str(n)
  total = 0
  for char in string:
    num = int(char)
    total += num
  return total

# # # # # # # # # #

def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x-1)
  
# # # # # # # # # #

def is_prime(x):
  if x < 2:
    return False
  else:
    for n in range(2, x-1):
      if x % n == 0:
        return False
    return True
  
# # # # # # # # # # 

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  for char in word:
    value = score[char]
    total += value
  return total

# # # # # # # # # #

def count(sequence, item):
  total = 0
  for ob in sequence:
    if ob == item:
      total += 1
  return total

# # # # # # # # # #

def purify(list):
  new_list = []
  for item in list:
    if item % 2 == 0:
      new_list.append(item)
  return new_list

# # # # # # # # # #

def product(list):
  total = 1
  for num in list:
    total *= num
  return total

# # # # # # # # # # 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for grade in scores:
    total += grade
  return total

def grades_average(grades_input):
  total = grades_sum(grades_input)
  avg = total / float(len(grades_input))
  return avg

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    dif = (average - score) ** 2
    variance += dif
  return variance / len(scores)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)

print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(variance)
print(grades_std_deviation(variance))

# # # # # # # # # #



# # # # # # # # # #
