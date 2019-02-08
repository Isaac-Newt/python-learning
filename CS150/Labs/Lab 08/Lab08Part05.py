# Isaac List - CS150 - October 26, 2018 - Lab 8 pt. 5

def atAndAfter(subject, target) :

    # Set up accumulation and counting variables, as well as termination condition
    newString = ''
    characterPosition = 0
    foundTarget = False
    
    # Consider every character
    while (characterPosition < len(subject)) :
        
        # If the character is the target, or if target has been found
        if subject[characterPosition] == target or foundTarget == True:
            # Add character to string
            newString += subject[characterPosition]
            # Target has been found
            foundTarget = True            
        else:
            # Don't add anything to string yet
            newString += ''
        
        characterPosition += 1
        
    return newString    

testSubject = input('Enter a subject string: ')
testTarget = input('Enter a target string: ')

print('<', atAndAfter(testSubject, testTarget), '>', sep = '')
