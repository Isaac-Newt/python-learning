# Isaac List - CS150 - November 14, 2018 - Lab 10 Pt. 3

# This program produces a custom number of files "out#.txt" which 
# each have a message in the form "This is message #X"

from simplefileio import *

def inputInt(prompt) :

    return int(input(prompt + '(an int) '))

numberOfMessages = inputInt('Enter the number of messages: ')

for messageNumber in range(1, numberOfMessages + 1) :
    
    name = "out" + str(messageNumber) + ".txt"
    print(name)
    openFile = fileopen(name, 'w')
    
    fileprint(openFile, 'This is message #', messageNumber)

    fileclose(openFile)