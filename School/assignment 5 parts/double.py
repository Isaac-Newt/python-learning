import image

def rotateImageLeft(original):
    # Create an empty image.
    # Width ==> 2*W, Height ==> 2*H
    doubled = image.EmptyImage(original.getHeight() * 2, original.getWidth() * 2)
    
    # For every x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Now comes the fun part... 
