# Isaac List - November 2, 2018 - Lab 9 Part 5


def filterOut(subjectList, filterValue) :
    # Creating identicle list
    newList = []
    for i in subjectList:
        newList.append(i)
        
    for i in range(len(newList)):
        if newList[i] == filterValue:
            subjectList.pop(i)
        

testSubjectA = [ ]
testSubjectB = [ 1 ]
testSubjectC = [ 1 ]
testSubjectD = [ 'aaa', 'bbb' ]
testSubjectE = [ 'aaa', 'bbb' ]
testSubjectF = [ 'aaa', 'bbb' ]
testSubjectG = [ 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1 ]
testSubjectH = [ 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1 ]

filterOut(testSubjectA, 1)
print(testSubjectA)
filterOut(testSubjectB, 2)
print(testSubjectB)
filterOut(testSubjectC, 1)
print(testSubjectC)
filterOut(testSubjectD, 'ccc')
print(testSubjectD)
filterOut(testSubjectE, 'bbb')
print(testSubjectE)
filterOut(testSubjectF, 'aaa')
print(testSubjectF)
filterOut(testSubjectG, 1)
print(testSubjectG)
filterOut(testSubjectH, 2)
print(testSubjectH)
