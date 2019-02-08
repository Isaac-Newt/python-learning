import image

def framedImage(original, thickness, red, green, blue):

    framedImage = image.EmptyImage(original.getWidth() + (2*thickness), original.getHeight() + (2*thickness))

    # Fill in framedImage background with border color
    for x in range(framedImage.getWidth()):
        for y in range(framedImage.getHeight()):
            borderPixel = image.Pixel(red, green, blue)
            framedImage.setPixel(x, y, borderPixel)

    # Print the image
    for x in range(thickness + 1, framedImage.getWidth() - thickness):
        for y in range(thickness + 1, framedImage.getHeight() - thickness):
            originalPixel = original.getPixel(x - (thickness +1), y - (thickness + 1))
            framedImage.setPixel(x, y, originalPixel)

    # Return the image
    return framedImage

imageFileName = input("Enter image file name: ")
originalPicture = image.Image(imageFileName)

originalWindow = image.ImageWin(imageFileName, originalPicture.getWidth(), originalPicture.getHeight())
originalPicture.draw(originalWindow)

greyFramedPicture = framedImage(originalPicture, 50, 128, 128, 128)
greyFramedWindow = image.ImageWin("Grey Framed" + imageFileName, greyFramedPicture.getWidth(), greyFramedPicture.getHeight())
greyFramedPicture.draw(greyFramedWindow)

originalWindow.exitonclick()
greyFramedWindow.exitonclick()
