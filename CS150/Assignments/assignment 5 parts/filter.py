import image

def filterImage(original, redFactor, greenFactor, blueFactor):
    # Create an empty image
    filtered = image.EmptyImage(original.getWidth(), original.getHeight())
    
    # For every x,y coordinated pixel
    for x in range(original.getWidth()):
        for y in range(original.getHeight()):
            # Name the pixel to do specific manipulation
            modifiedPixel = original.getPixel(x,y)
            
            # Modify the colors, but first check to see if result will be higher
            # than 255.  If it is, set to 255.  
            # If negative, set value to 0
            
            # Red
            if (modifiedPixel.getRed() * redFactor > 255):
                modifiedPixel.setRed(255)
            elif redFactor < 0:
                modifiedPixel.setRed(0)
            else:
                modifiedPixel.setRed(modifiedPixel.getRed() * redFactor)
                
            # Green
            if (modifiedPixel.getGreen() * greenFactor > 255):
                modifiedPixel.setGreen(255)
            elif greenFactor < 0:
                modifiedPixel.setGreen(0)
            else:
                modifiedPixel.setGreen(modifiedPixel.getGreen() * greenFactor)
            
            # Blue
            if (modifiedPixel.getBlue() * blueFactor > 255):
                modifiedPixel.setBlue(255)
            elif blueFactor < 0:
                modifiedPixel.setBlue(0)
            else:
                modifiedPixel.setBlue(modifiedPixel.getBlue() * blueFactor)
            
            # Set the current pixel in the image to modifiedPixel's values
            filtered.setPixel(x, y, modifiedPixel)
            
    # Return the filtered image
    return filtered
