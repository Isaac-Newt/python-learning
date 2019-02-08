# Isaac List - CS150 - November 14, 2018 - Lab 10 Pt. 2

# This file reads in floats 

from simplefileio import *

def inputFloat(prompt) :

    return float(input(prompt + '(a float) '))

# Files to be used
# Input source
inputFile = fileopen("in02.txt", "r")
# Output destination
outputFile = fileopen("out02.txt", "w")

# Get a value from the input file to write to the output file 
value = fileinput(inputFile)

while value != None :
    # Print current value to the output file
    fileprint(outputFile, value)
    # Get the next value
    value = fileinput(inputFile)

fileclose(inputFile)
fileclose(outputFile)