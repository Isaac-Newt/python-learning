# Isaac List - November 27, 2018

# This program takes three inputs, corresponding to RGB
# values (0-255) and converts them to a hex color code.

# Inputs
print("Enter three integers between 0 and 255 inclusive.")
red = int(input("Enter a 'red' value: "))
green = int(input("Enter a 'green' value: "))
blue = int(input("Enter a 'blue' value: "))

# Make string for decimal input for pretty print answer
rgbValue = "(" + str(red) + "," + str(green) + "," + str(blue) + ")"

# Conversion to hexadecimal
redHex = hex(red)
greenHex = hex(green)
blueHex = hex(blue)

# Further conversion for proper stringing
redHex = str(redHex)[2:]
greenHex = str(greenHex)[2:]
blueHex = str(blueHex)[2:]

# Make sure hex values are all two digits
if len(redHex) < 2:
    redHex = "0" + redHex

if len(greenHex) < 2:
    greenHex = "0" + greenHex

if len(blueHex) < 2:
    blueHex = "0" + blueHex

# Make hex color code
hexcode = "#" + redHex + greenHex + blueHex

# Print a nice little response
print(rgbValue, "in hex color code is", hexcode)

