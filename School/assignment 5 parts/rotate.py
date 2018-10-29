import image

def rotateImageLeft(original):
    # Create an empty image.
    # Width ==> Height, Height ==> Width
    rotated = image.EmptyImage(original.getHeight(), original.getWidth())
    
    # For every x,y coordinated pixel in the new empty image
    for x in range(rotated.getWidth()):
        for y in range(rotated.getHeight()):
            # Define the pixel from the original image to use
            # This pixel will have x = (original x - 1) - (target x)
            # and y = (original y - 1) - (target y)
            originalOffsetPixel = original.getPixel((original.getWidth() - 1 - x), (original.getHeight() - 1 -y))
            
            # Set the current target pixel in "rotated" to the offset original
            rotated.setPixel(x, y, originalOffsetPixel) 
    
    # Return the rotated image
    return rotated