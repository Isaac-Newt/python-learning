# Isaac List - CS150 - October 19, 2018
#
# Lab 7 - Part 1

import image

picture-bear = image.Image('bigredbear.gif')
picture-eniac = image.Image('Eniac.gif')
picture-Olin = image.Image('Olin.gif')

window-bear = \
    image.ImageWin(
        'Big Red Bear',
        picture.getWidth(),
        picture.getHeight()
        )

window-eniac = \
    image.ImageWin(
        'Enaic',
        picture.getWidth(),
        picture.getHeight()
        )

window-Olin = \
    image.ImageWin(
        'Olin',
        picture.getWidth(),
        picture.getHeight()
        )

picture-bear.draw(window-bear)
picture-enaic.draw(Enaic)
picture-Olin.draw(Olin)

window-bear.exitonclick()
window-enaic.exitonclick()
window-Olin.exitonclick()
