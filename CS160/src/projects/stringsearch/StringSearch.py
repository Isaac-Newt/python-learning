# Isaac List - CS160A - Exercise1 - February 6, 2019
# 
# Find the first non-repeated character in an arbitrary string.
# This program uses a dictionary to count the occurances of the
# string's characters, finds those that occur only once, and 
# constructs a list, the answer then being item 0 of that list.
#
# Note: Works as expected in 3.5.x, 3.6.x, and 3.7.x, meaning
# it does not have the same drawback as version 1 with order.

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

    # Set up while loop
    count = 0
    found = False
    # This will be returned by the function
    answer = ""
    while count < len(string) and found == False:
        # Because it looks nicer in the if statement
        key = string[count]
        if dictionaryOfCharacters[key] == 1:
            # Set answer to the current character
            answer = key
            # End the loop
            found = True
        # Go on to the next character
        count += 1

    return answer

string = input("Enter a string: ")

print("The first non-repeated character is:", findFirstNonRepeat(string))