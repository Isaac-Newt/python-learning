import image

def reflectImage(original):
    # Create an empty image
    reflected = image.EmptyImage(original.getWidth(), original.getHeight())
    
    # For each x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Invert across the y axis, so negative x, same y
            reflected.setPixel(original.getHeight() - 1 - x, y, original.getPixel(x,y))
            
    # return the reflected image
    return reflected
