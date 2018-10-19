import image


def duplicateImage(original) :

    duplicate = image.EmptyImage(original.getWidth(), original.getHeight())

    for x in range(original.getWidth()) :
        for y in range(original.getHeight()) :

            duplicate.setPixel(x, y, original.getPixel(x, y))

    return duplicate


originalPicture = image.Image('bigredbear.gif')

originalWindow = \
    image.ImageWin(
        'Big Red Bear',
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

originalPicture.draw(originalWindow)

duplicatePicture = duplicateImage(originalPicture)

duplicateWindow = \
    image.ImageWin(
        'Duplicate Big Red Bear',
        duplicatePicture.getWidth(),
        duplicatePicture.getHeight()
        )

duplicatePicture.draw(duplicateWindow)

originalWindow.exitonclick()
duplicateWindow.exitonclick()
