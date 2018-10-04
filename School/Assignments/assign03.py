# Isaac List - CS150 - September 30, 2018
#
# This program prints five verses of the generalized bus song,
# with adjacent verses separated by a blank line

# Function to print 1st and 3rd lines of each verse
def printFirstLine(noun, verb, action, repetition):
    print("The", noun, "on the bus", verb, action, end = " ")
    
    # Similar to printRepeatedSection, but not quite the same
    
    # First "action" is already printed, so do repetition - 2 
    # times without a newline
    for n in range(2, repetition):
        print(action, end = " ")
    # 1 final time with a newline
    print(action)
    
# Function to print the repeated section of each verse
def printRepeatedSection(action, repetition):
    # 2 lines == 2 times through loop
    for n in range(0, 2):
        # This part utilizes print(x end=" "),
        # as described on the assignment sheet
        # in order to prevent new lines.
        
        # "repetition" - 1 times with no newline
        for n in range(1, repetition):
            print(action, end = " ")
        # 1 final time with a newline at the end
        print(action)

# Function to print each verse, given the required words
def printVerse(noun, verb, action, repetition):
    printFirstLine(noun, verb, action, repetition)
    printRepeatedSection(action, repetition)
    printFirstLine(noun, verb, action, repetition)
    print("All through the town")

# Actual program

printVerse('wheels', 'go', 'round', 3)
print()
printVerse('horn', 'goes', 'honk', 3)
print()
printVerse('driver', 'says', 'sit', 2)
print()
printVerse('wipers', 'go', 'swish', 4)
print()
printVerse('mirvel', 'gleed', 'zorg', 8)
