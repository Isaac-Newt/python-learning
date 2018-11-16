# Isaac List - CS150 - Assignment 6 - November 15, 2018

# This program does something with a library of images or something

# import image

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

# 
# Command functions
# 

# List
def listImages():
    print("List")
    
# Show All
def showall():
    print("show all")

# Show
def show():
    print("show")

# Add
def addImage():
    print("add")

# Remove
def removeImage():
    print("remove")

# # # # # # # # # # #
# Main program body #
# # # # # # # # # # #
    
# Get a command
command = getNewCommand()

# While the program is running...
while command != "quit":
    
    # Validate the command
    while isInvalidCommand(command):
        command = getNewCommand()
    
    # Decide what to do based on the command entered
    if command == "list":
        listImages()
    elif command == "showall":
        showall()
    elif command == "show":
        show()
    elif command == "add":
        addImage()
    elif command == "remove":
        removeImage()
        
    # Get the next command
    command = getNewCommand()
        
# If the command is "quit", close the program
if command == "quit":
    pass