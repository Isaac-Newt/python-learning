# Isaac List - CS150 - Assignment 7 - December 1, 2018

# This solution to Assignment makes use of a list of lists-of-two-elements to 
# keep track of the collection of images in the variable fileNamesAndTitles.   
# When there are n images in the collection,
#
#     fileNamesAndTitles =
#         [ [ imageFileNameString0, imageTitleString0 ],
#             [ imageFileNameString1, imageTitleString1 ],
#             ... ,
#             [ imageFileNameStringn-1, imageTitleStringn-1 ]
#             ]

# Import necessary modules
import image
from simplefileio import *

# My functions

# Saves the current list of image files and names to a file created by the user
def saveAlbum(currentAlbumList):
    # choose file name
    newFileName = input("Please enter a file name to save album to: ")
    
    # open the file (write mode)
    newAlbumFile = fileopen(newFileName, "w")
    
    # for each item in the list currentAlbumList, print the filename (0) and the
    # title (1) to the newAlbumFile. This will alternate lines filename/title.
    for image in currentAlbumList:
        fileprint(newAlbumFile, image[0])
        fileprint(newAlbumFile, image[1])
    
    # save (close) the file
    fileclose(newAlbumFile)

# After erasing the current loaded album, loads a previously created list of image
# files and names from a file, adding them similar to as in the addImage function.
def loadAlbum(currentAlbumList):
    # remove current images in currentAlbumLists
    del currentAlbumList[:]
    
    # choose file name
    chosenFileName = input("Please enter the name of an album file: ")
    
    # open the file (read mode)
    subjectAlbumFile = fileopen(chosenFileName, "r")
    
    # read each line to get a filename or a title
    # make every 2 lines into a 2-item list (name/title pair)
    # add each pair to the list fileNamesAndTitles
    
    fileIsNotFinished = True
    while fileIsNotFinished:
        # file name
        fileName = fileinput(subjectAlbumFile)
        # file title
        title = fileinput(subjectAlbumFile)
        
        # Check to see if end of file has been reached
        if fileName == None:
            fileIsNotFinished = False
        else:
            # add mini list to list 
            currentAlbumList.append([ fileName, title ])            
    
    # close the file
    fileclose(subjectAlbumFile)

# Pre-written functions

def isValidImageNumber(imageFileNamesAndTitles, imageNumber) :
    """Determines if imageNumber (an integer) is a valid image number wrt imageFileNamesAndTitles (a list of lists of two strings)"""

    return 0 <= imageNumber < len(imageFileNamesAndTitles)


def showOneImage(imageFileName, imageTitle) :
    """Displays the image in the file named by imageFileName (a string) in a window having the title imageTitle (a string), waiting for a click on the window to close the window and then continue"""

    theImageToShow = image.Image(imageFileName)

    window = \
        image.ImageWin(imageTitle, theImageToShow.getWidth(), theImageToShow.getHeight())

    theImageToShow.draw(window)

    window.exitonclick()


def listImages(imageFileNamesAndTitles) :
    """Prints a numbered list of the images and titles described collectively by imageFileNamesAndTitles (a list of lists of two strings)"""

    for imageNumber in range(len(imageFileNamesAndTitles)) :
        print(
            '(',
            imageNumber,
            ') ',
            imageFileNamesAndTitles[ imageNumber ][ 0 ],
            ': ',
            imageFileNamesAndTitles[ imageNumber ][ 1 ],
            sep = ''
            )


def showAllImages(imageFileNamesAndTitles) :
    """Displays in sequence the images and titles in the files and titles named in imageFileNamesAndTitles (a list of lists of two strings), waiting for a click on each window to close the window and then continue to the next image"""

    for imageNumber in range(len(imageFileNamesAndTitles)) :
        showOneImage(
            imageFileNamesAndTitles[ imageNumber ][ 0 ],
            imageFileNamesAndTitles[ imageNumber ][ 1 ]
            )


def addImage(imageFileNamesAndTitles) :
    """Prompts the user and then inputs fileName (a string) and a title (a string) and adds them to imageFileNamesAndTitles (a list of lists of two strings)"""

    fileName = input('Enter the image file name: ')
    title = input('Enter the image\'s title: ')

    imageFileNamesAndTitles.append([ fileName, title ])


def showImage(imageFileNamesAndTitles) :
    """Prompts the user and then inputs imageNumber (an integer), validates that imageNumber is a position within imageFileNamesAndTitles (a list of lists of two strings), and displays the image whose information is given by the imageNumber-th item in imageFileNamesAndTitles"""

    imageNumber = int(input('Enter the # of the image to show: '))

    if not isValidImageNumber(imageFileNamesAndTitles, imageNumber) :

        print('**** That\'s not a valid image number')

    else :

        showOneImage(
            imageFileNamesAndTitles[ imageNumber ][ 0 ],
            imageFileNamesAndTitles[ imageNumber ][ 1 ]
            )


def removeImage(imageFileNamesAndTitles) :
    """Prompts the user and then inputs imageNumber (an integer), validates that imageNumber is a position within imageFileNamesAndTitles (a list of lists of two strings), and removes the information given by the imageNumber-th item in imageFileNamesAndTitles"""

    imageNumber = int(input('Enter the # of the image to remove: '))

    if not isValidImageNumber(imageFileNamesAndTitles, imageNumber) :

        print('**** That\'s not a valid image number')

    else :

        imageFileNamesAndTitles.pop(imageNumber)


#
# Let fileNamesAndTitles represent an empty collection of images and titles
#

fileNamesAndTitles = [ ]

#
# Process a sequence of collection-of-images commands entered by the user, using and
# updating fileNamesAndTitles as necessary
#

#
# Let command be a collection-of-images command entered by the user
#

command = input('Command? ')

while command != 'quit' :

    #
    # Process command
    #

    if command == 'list' :
        listImages(fileNamesAndTitles)

    elif command == 'showall' :
        showAllImages(fileNamesAndTitles)

    elif command == 'add' :
        addImage(fileNamesAndTitles)

    elif command == 'show' :
        showImage(fileNamesAndTitles)

    elif command == 'remove' :
        removeImage(fileNamesAndTitles)
        
    elif command == 'save' :
        saveAlbum(fileNamesAndTitles)
        
    elif command == 'load' :
        loadAlbum(fileNamesAndTitles)

    else :
        print('**** There\'s no such command as "' + command + '"')

    #
    # Let command be a collection-of-images command entered by the user
    #

    command= input('Command? ')
