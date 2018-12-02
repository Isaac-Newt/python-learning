# Isaac List - CS150 - October 19, 2018
# 
# Lab 7 Part 3

import image

originalPicture = image.Image('bigredbear.gif')

originalWindow = \
    image.ImageWin(
        'Big Red Bear',
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

originalPicture.draw(originalWindow)

redPicture = \
    image.EmptyImage(
        originalPicture.getWidth(),
        originalPicture.getHeight()
        )

redWindow = \
    image.ImageWin(
        'Big, Very Red Bear',
        dimPicture.getWidth(),
        dimPicture.getHeight()
        )

for x in range(originalPicture.getWidth()) :
    for y in range(originalPicture.getHeight()) :

        redPixel = originalPicture.getPixel(x, y)

        redPixel.setRed(dimPixel.getRed())
        redPixel.setGreen(0)
        redPixel.setBlue(0)

        redPicture.setPixel(x, y, dimPixel)

redPicture.draw(redWindow)

originalWindow.exitonclick()
redWindow.exitonclick()
