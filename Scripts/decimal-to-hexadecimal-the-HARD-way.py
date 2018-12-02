# Isaac List - November 28, 2018

# Decimal to Hexadecimal the hard way

def decimalToHexadecimal(integer):
    hexstring = ""

    # Basic checks
    if integer <= 0:
        hexstring += "00"

    # If less than 16
    else:
        # find 16's position
        decimalToHexadecimal(integer / 16)

        # Add prefacing 0
        hexstring += "0"
        newInt = (integer % 16)
        # find "1's'" position digit
        if newInt < 10:
            hexstring += str(newInt)
        elif newInt == 10:
            hexstring += "A"
        elif newInt == 11:
            hexstring += "B"
        elif newInt == 12:
            hexstring += "C"
        elif newInt == 13:
            hexstring += "D"
        elif newInt == 14:
            hexstring += "E"
        elif newInt == 15:
            hexstring += "F"

    return hexstring


# Interactivity
number = 0
while number >= 0:
    number = int(input("Enter an int between 0 and 255 inclusive: "))
    print(decimalToHexadecimal(number))
