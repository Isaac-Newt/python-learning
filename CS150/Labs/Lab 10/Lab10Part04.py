# Isaac List - CS150 - Lab 10 Pt 4 - November 16, 2018

# This program takes lines from one file, and 
# creates a new file with the lines in reverse order.

from simplefileio import *

# Set up a list to add each line to
listOfLines = []

# Choose input source
inputFile = fileopen("in04.txt", "r")

# get the first line
line = fileinput(inputFile)

# While there are lines in the input file
while line != None:
    # add the line to the list
    listOfLines.append(line)
    # get the next line
    line = fileinput(inputFile)    
    
# Close the input file
fileclose(inputFile)    

# Open an output file
outputFile = fileopen("out04.txt", "w")

# Start an index
index = -1

# Go through list backwards, starting at last line
while index >= -len(listOfLines):
    # Get line from the list in reverse order
    lineFromEnd = listOfLines[index]
    
    # Print each line to the output file
    fileprint(outputFile, lineFromEnd)
    
    # Update the index
    index -= 1
    
# Close the file 
fileclose(outputFile)