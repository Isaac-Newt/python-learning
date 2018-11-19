# Isaac List - CS150 - Assignment 6 - November 15, 2018

# This program does something with a library of images or something

import image

# # # # # # # # # # #
# Program Functions #
# # # # # # # # # # #

# 
# Input functions
# 

# Input command
def getNewCommand():
    command = input("Enter a command: ")
    return command    

# Returns True if candidate is not one of the valid commands
def isInvalidCommand(candidate):
    if candidate == "list":
        return False
    elif candidate == "showall":
        return False
    elif candidate == "show":
        return False
    elif candidate == "add":
        return False
    elif candidate == "remove":
        return False   
    elif candidate == "quit":
        return False  
    else:
        print("Please enter a valid command")
        return True

# Index validation for show command
def indexNotInRange(candidate, fileList):
    # If candidate is out of range, return True
    if candidate >= len(fileList):
        return True
    else:
        return False

# 
# Command functions
# 

# List
def listImages(nameList, fileList):
    # Lists the image index (an int), and the 
    # object at that index in both lists
    print("List")
    
    # Lists are the same length, so for number in the length of one of them
    for index in range(len(nameList)):
        print(index, end = ' ')
        print(fileList[index] + ":", end = ' ')
        print(nameList[index])
    
# Show All
def showall(nameList, fileList):
    print("show all")
    # Show each image in order, and leave up until clicked.
    # Then, exit the image and display the next one.
    for index in range(len(fileList)):
        # Get the image
        imageToShow = image.Image(fileList[index])
        
        # Image name
        nameOfImage = nameList[index]
        
        # Draw the image
        window = image.ImageWin(nameOfImage, imageToShow.getWidth(), imageToShow.getHeight())
        imageToShow.draw(window)
        window.exitonclick()

# Show
def show(nameList, fileList):
    print("show")
    # Get image choice
    indexToShow = int(input("Enter number of image to show: "))
    
    # Check to see if in range
    while indexNotInRange(indexToShow, fileList):
        print("Image number not available.")
        indexToShow = int(input("Enter number of image to show: "))
    
    # Image name
    nameOfImage = nameList[indexToShow]
    
    # Load image from selected index
    imageToShow = image.Image(fileList[indexToShow])
    
    # Draw the image
    window = image.ImageWin(nameOfImage, imageToShow.getWidth(), imageToShow.getHeight())
    imageToShow.draw(window)
    window.exitonclick()

# Add
def addImage(nameList, fileList):
    print("add")
    # Get file name
    filename = input("Enter the file name of the image: ")
    name = input("Enter the image's name: ")
    # Add file and name to respective lists
    nameList.append(name)
    fileList.append(filename)

# Remove
def removeImage(nameList, fileList):
    print("remove")
    # Get image index to remove, and remove from each list
    removeIndex = int(input("Enter number of image to remove: "))
    nameList.pop(removeIndex)
    fileList.pop(removeIndex)

# # # # # # # # # # #
# Main program body #
# # # # # # # # # # #
    
# Create lists for names, filenames, of files
listOfImageNames = []
listOfImageFiles = []
    
# Get a command
command = getNewCommand()

# While the program is running...
while command != "quit":
    
    # Validate the command
    while isInvalidCommand(command):
        command = getNewCommand()
    
    # Decide what to do based on the command entered
    if command == "list":
        listImages(listOfImageNames, listOfImageFiles)
    elif command == "showall":
        showall(listOfImageNames, listOfImageFiles)
    elif command == "show":
        show(listOfImageNames, listOfImageFiles)
    elif command == "add":
        addImage(listOfImageNames, listOfImageFiles)
    elif command == "remove":
        removeImage(listOfImageNames, listOfImageFiles)
        
    # Get the next command
    command = getNewCommand()