# Isaac List - November 28, 2018

# Decimal to Hexadecimal 

def decimalToHexadecimal(integer):
    # Set up hexadecimal string
    hexstring = ""

    # Basic checks
    if integer == 0:
        hexstring += "00"

    # If less than 16
    elif integer < 16:
        # Add prefacing 0
        hexstring += "0"

        # find "1's'" position digit
        if integer < 10:
            hestring += str(integer)
        elif integer == 10:
            hexstring += "A"
        elif integer == 11:
            hexstring += "B"
        elif integer == 12:
            hexstring += "C"
        elif integer == 13:
            hexstring += "D"
        elif integer == 14:
            hexstring += "E"
        elif integer == 15:
            hexstring += "F"

    # 16's
    elif integer % 16 == 0:
        if integer / 16 < 10:
            hexstring += str(integer)
        elif integer / 16 == 10:
            hexstring += "A"
        elif integer / 16 == 11:
            hexstring += "B"
        elif integer / 16 == 12:
            hexstring += "C"
        elif integer / 16 == 13:
            hexstring += "D"
        elif integer / 16 == 14:
            hexstring += "E"
        elif integer / 16 == 15:
            hexstring += "F"

