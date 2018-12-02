# Isaac List - CS150 - October 19, 2018
# 
# Lab 7 Part 2

import image

pictureName = input("What image would you like to display?: ")

picture = image.Image(pictureName)

window = \
    image.ImageWin(
        pictureName,
        picture.getWidth(),
        picture.getHeight()
        )

picture.draw(window)

window.exitonclick()
