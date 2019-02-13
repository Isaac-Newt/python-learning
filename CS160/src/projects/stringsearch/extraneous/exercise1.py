# Isaac List - CS160A - Exercise1 - February 6, 2019
# 
# Find the first non-repeated character in an arbitrary string.
# This program uses a dictionary to count the occurances of the
# string's characters, finds those that occur only once, and 
# constructs a list, the answer then being item 0 of that list.
#
# Note: Works as expected in 3.6.x and 3.7.x, but not in 3.5.x,
# because versions >= 3.6 have an ordered listing within the dict
# object, but versions <= 3.5 do not.  

def findFirstNonRepeat(string):

    dictionaryOfCharacters = {}

    # Count occurances of each character in the string
    for int in range(len(string)):
        if string[int] in dictionaryOfCharacters:
            dictionaryOfCharacters[string[int]] += 1
        else:
            dictionaryOfCharacters[string[int]] = 1

    # Debugging
    print(dictionaryOfCharacters)

    # Find the first key with a value of 1
    listOfKeys = []

    for key in dictionaryOfCharacters:
        if dictionaryOfCharacters[key] == 1:
            listOfKeys.append(key)
            print(listOfKeys)

    # Answer is the first item in the list
    answer = listOfKeys[0]
    return answer

string = input("Enter a string: ")

print("The first non-repeated character is:", findFirstNonRepeat(string))