import image

def rotateImage(original):
    rotated = image.EmptyImage(original.getWidth(), original.getHeight())
    
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            rotated.setPixel(original.getWidth() - 1 - x, original.getHeight() - 1 - y, original.getPixel(x, y))
            
    return rotated


originalPicture = image.Image('bigredbear.gif')

originalWindow = \
    image.ImageWin(
        'Big Red Bear',
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

originalPicture.draw(originalWindow)

rotatedPicture = rotateImage(originalPicture)

rotatedWindow = \
    image.ImageWin(
        'Rotated Big Red Bear',
        rotatedPicture.getWidth(),
        rotatedPicture.getHeight()
        )

rotatedPicture.draw(rotatedWindow)

originalWindow.exitonclick()
rotatedWindow.exitonclick()
