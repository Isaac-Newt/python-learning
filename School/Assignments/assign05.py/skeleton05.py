import image


def inputFloat(prompt) :

    return float(input(prompt + '(a float) '))


def loadImage(fileName) :

    try :

        loadedImage = image.Image(fileName)

    except :

        print("**** Can't load from file", fileName)

        loadedImage = None

    return loadedImage


def saveImage(imageToSave, fileName) :

    try :

        imageToSave.save(fileName)

    except :

        print("**** Can't save to file", fileName)


def showImage(imageToShow) :

    window = image.ImageWin('', imageToShow.getWidth(), imageToShow.getHeight())

    imageToShow.draw(window)

    window.exitonclick()


def invertImage(original) :

    inverted = image.EmptyImage(original.getWidth(), original.getHeight())

    for x in range(original.getWidth()) :
        for y in range(original.getHeight()) :

            inverted.setPixel(x, original.getHeight() - 1 - y, original.getPixel(x, y))

    return inverted


def reflectImage(original) :

    ####
    #### COMPLETE THE FUNCTION reflectImage
    ####


def filterImage(original, redFactor, greenFactor, blueFactor) :

    ####
    #### COMPLETE THE FUNCTION filterImage
    ####


def rotateImageLeft(original) :

    ####
    #### COMPLETE THE FUNCTION rotateImageLeft
    ####


def doubleImage(original) :

    ####
    #### COMPLETE THE FUNCTION doubleImage
    ####


currentImage = None

command = input('Enter a command: ')

while command != 'quit' :

    if command == 'load' :

        fileName = input('Enter the name of the image file to load from: ')

        currentImage = loadImage(fileName)

    elif command == 'save' :

        if currentImage != None :

            fileName = input('Enter the name of the image file to save to: ')
            saveImage(currentImage, fileName)

    elif command == 'show' :

        if currentImage != None :
            showImage(currentImage)

    elif command == 'invert' :

        if currentImage != None :
            currentImage = invertImage(currentImage)

    elif command == 'reflect' :

        if currentImage != None :
            currentImage = reflectImage(currentImage)

    elif command == 'filter' :

        if currentImage != None :
            redAdjustment = inputFloat('Enter the red-adjustment factor: ')
            greenAdjustment = inputFloat('Enter the green-adjustment factor: ')
            blueAdjustment = inputFloat('Enter the blue-adjustment factor: ')
            currentImage = \
                filterImage(currentImage, redAdjustment, greenAdjustment, blueAdjustment)

    elif command == 'rotate' :

        if currentImage != None :
            currentImage = rotateImageLeft(currentImage)

    elif command == 'double' :

        if currentImage != None :
            currentImage = doubleImage(currentImage)

    else :

        print('**** No such command as', command)

    command = input('Enter a command: ')
