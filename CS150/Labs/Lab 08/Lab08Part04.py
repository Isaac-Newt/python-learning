# Isaac List - CS150 - October 26, 2018 - Lab 8 pt. 4

def before(subject, target) :

    # Set up accumulation and counting variables, as well as termination condition
    newString = ''
    characterPosition = 0
    foundTarget = False
    
    # While the characterPosition is in range, and the target has not yet been found:
    while (characterPosition < len(subject)) and (not foundTarget) :
        
        # If the character is the target, stop adding letters
        if subject[characterPosition] == target:
            newString += ''
            foundTarget = True
        else:
            newString += subject[characterPosition]
        
        characterPosition += 1
        
    return newString

testSubject = input('Enter a subject string: ')
testTarget = input('Enter a target string: ')

print('<', before(testSubject, testTarget), '>', sep = '')
