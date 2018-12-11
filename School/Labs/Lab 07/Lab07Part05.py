import image


originalPicture = image.Image('bigredbear.gif')

originalWindow = \
    image.ImageWin(
        'Big Red Bear',
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

originalPicture.draw(originalWindow)

dimPicture = \
    image.EmptyImage(
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

dimWindow = \
    image.ImageWin(
        'Dim Big Red Bear',
        dimPicture.getWidth(),
        dimPicture.getHeight()
        )

for x in range(originalPicture.getWidth()) :
    for y in range(originalPicture.getHeight()) :

        dimPixel = originalPicture.getPixel(x, y)

        dimPixel.setRed(dimPixel.getRed() // 4)
        dimPixel.setGreen(dimPixel.getGreen() // 4)
        dimPixel.setBlue(dimPixel.getBlue() // 4)

        dimPicture.setPixel(x, y, dimPixel)

dimPicture.draw(dimWindow)

redPicture = image.EmptyImage(originalPicture.getWidth(), originalPicture.getHeight())

redWindow = image.ImageWin("Red Red Bear",originalPicture.getWidth(), originalPicture.getHeight())

for x in range(originalPicture.getWidth()):
    for y in range(originalPicture.getHeight()):
        redPixel = originalPicture.getPixel(x, y)
        redPixel.setRed(redPixel.getRed())
        redPixel.setGreen(0)
        redPixel.setBlue(0)
        
        redPicture.setPixel(x, y, redPixel)

redPicture.draw(redWindow)

originalWindow.exitonclick()
dimWindow.exitonclick()
redWindow.exitonclick()
