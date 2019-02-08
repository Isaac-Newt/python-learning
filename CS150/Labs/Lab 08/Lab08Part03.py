# Isaac List - CS150 - October 26, 2018 - Lab 8 pt. 3

def subst(subject, target, replacement) :

    # Set up accumulation and counting variables
    newString = ''
    characterPosition = 0
    
    while characterPosition < len(subject):
        
        # If the character is the target, replace it, otherwise add letters as normal
        if subject[characterPosition] == target :
            newString += replacement
        else:
            newString += subject[characterPosition]
            
        characterPosition += 1
        
    return newString

testSubject = input('Enter a subject string: ')
testTarget = input('Enter a target string: ')
testReplacement = input('Enter a replacement string: ')

print('<', subst(testSubject, testTarget, testReplacement), '>', sep = '')
