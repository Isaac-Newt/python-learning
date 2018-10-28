import image

def rotateImageLeft(original):
    # Create an empty image.
    # Width ==> Height, Height ==> Width
    rotated = image.EmptyImage(original.getHeight(), original.getWidth())
    
    # For every x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Now comes the fun part... 
