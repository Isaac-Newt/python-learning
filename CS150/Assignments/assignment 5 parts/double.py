import image

def doubleImage(original):
    # Create an empty image.
    # Width ==> 2*W, Height ==> 2*H
    doubled = image.EmptyImage(original.getHeight() * 2, original.getWidth() * 2)
    
    # For every x,y coordinated pixel in the new empty image
    for x in range(doubled.getWidth()):
        for y in range(doubled.getHeight()):
            doubled.setPixel(2x, 2y, original.getPixel(x,y))
            doubled.setPixel(2x + 1, 2y, original.getPixel(x,y))
            doubled.setPixel(2x, 2y + 1, original.getPixel(x,y))
            doubled.setPixel(2x + 1, 2y + 1, original.getPixel(x,y))
    
    return doubled
