# Isaac List - CS150 - October 26, 2018 - Lab 8 pt. 2

def doubleEach(subject) :
    
    # Set up accumulation and counting variables
    newString = ''
    characterPosition = 0
    
    while characterPosition < len(subject):
        newString += subject[characterPosition]
        newString += subject[characterPosition]
        
        characterPosition += 1
        
    return newString

testSubject = input('Enter a subject string: ')

print('<', doubleEach(testSubject), '>', sep = '')
