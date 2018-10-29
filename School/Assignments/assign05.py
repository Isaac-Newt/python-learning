# Isaac List - CS150 - October 28, 2018
# 
# Assignment 5 - Image Manipulation
# This program includes several functions allowing for the manipulation of images.

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

# Reflected Image Function
def reflectImage(original):
    # Create an empty image
    reflected = image.EmptyImage(original.getWidth(), original.getHeight())
    
    # For each x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Invert across the y axis, so negative x, same y
            reflected.setPixel(original.getWidth() - 1 - x, y, original.getPixel(x,y))
            
    # return the reflected image
    return reflected

# Filtered Image Function
def filterImage(original, redFactor, greenFactor, blueFactor) :
    # Create an empty image
    filtered = image.EmptyImage(original.getWidth(), original.getHeight())
    
    # For every x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Name the pixel to do specific manipulation
            modifiedPixel = original.getPixel(x,y)
            
            # Modify the colors, but first check to see if result will be higher
            # than 255.  If it is, set to 255.  
            # If negative, set value to 0
            
            # When setting the target pixel's R/G/B value, said value must be an
            # int.  This is accomplished by using the int() method on the value.
            
            # Red
            if (modifiedPixel.getRed() * redFactor > 255):
                modifiedPixel.setRed(255)
            elif redFactor < 0:
                modifiedPixel.setRed(0)
            else:
                modifiedPixel.setRed(int(modifiedPixel.getRed() * redFactor))
                
            # Green
            if (modifiedPixel.getGreen() * greenFactor > 255):
                modifiedPixel.setGreen(255)
            elif greenFactor < 0:
                modifiedPixel.setGreen(0)
            else:
                modifiedPixel.setGreen(int(modifiedPixel.getGreen() * greenFactor))
            
            # Blue
            if (modifiedPixel.getBlue() * blueFactor > 255):
                modifiedPixel.setBlue(255)
            elif blueFactor < 0:
                modifiedPixel.setBlue(0)
            else:
                modifiedPixel.setBlue(int(modifiedPixel.getBlue() * blueFactor))
            
            # Set the current pixel in the image to modifiedPixel's values
            filtered.setPixel(x, y, modifiedPixel)
            
    # Return the filtered image
    return filtered

# Rotated image function
def rotateImageLeft(original) :
    # Create an empty image.
    # Width ==> Height, Height ==> Width
    rotated = image.EmptyImage(original.getHeight(), original.getWidth())
    
    # For every x,y coordinated pixel in the new empty image
    for x in range(rotated.getWidth()):
        for y in range(rotated.getHeight()):
            # Define the pixel from the original image to use
            # This pixel will have x = (original x - 1) - (target x)
            # and y = (original y - 1) - (target y)
            originalOffsetPixel = original.getPixel((original.getWidth() - 1 - y), x)
            
            # Set the current target pixel in "rotated" to the offset original
            rotated.setPixel(x, y, originalOffsetPixel) 
    
    # Return the rotated image
    return rotated

# doubled image funciton
def doubleImage(original) :
    # Create an empty image.
    # Width ==> 2*W, Height ==> 2*H
    doubled = image.EmptyImage(original.getWidth() * 2, original.getHeight() * 2)
  
    # For every x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            originalPixel = original.getPixel(x, y)
            
            # Fill four pixels with the original pixel's value.  
            # These pixels are defined by the coordinates:
            # (2x, 2y)      (2x + 1, 2y)
            # (2x, 2y + 1)  (2x + 1, 2y + 1)
            doubled.setPixel(2 * x, 2 * y, originalPixel)
            doubled.setPixel((2 * x) + 1, 2 * y, originalPixel)
            doubled.setPixel(2 * x, (2 * y) + 1, originalPixel)
            doubled.setPixel((2 * x) + 1, (2 * y) + 1, originalPixel)
    
    # Return the doubled image
    return doubled


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
