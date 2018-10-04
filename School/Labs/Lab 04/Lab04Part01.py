# Isaac List - CS150 - September 24, 2018
#
# This program draws a square wave given parameters 
# for dimensions and repititions.

import turtle

# Useful stuff
def inputInt(prompt) :
    value = input(prompt + '(an int) ')
    value = int(value)

    return value

# Another useful thing
def inputFloat(prompt) :
    value = input(prompt + '(a float) ')
    value = float(value)

    return value

# Drawing function
def drawSquareWave(valleyWidth, peakHeight, peakWidth, numberOfCycles):
    wn = turtle.Screen()
    dan = turtle.Turtle()
    
    # Run drawing pattern [numberOfCycles] times
    for n in range(0, numberOfCycles):
        dan.forward(valleyWidth)
        dan.left(90)
        dan.forward(peakHeight)
        dan.right(90)
        dan.forward(peakWidth) 
        dan.right(90)
        dan.forward(peakHeight)
        dan.left(90)

# Get inputs
valleyWidth = inputFloat('Enter the width of the valleys: ')
peakHeight = inputFloat('Enter the height of the peaks: ')
peakWidth = inputFloat('Enter the width of the peaks: ')
numberOfCycles = inputInt('Enter the # of cycles: ')

# Actually run the drawing
drawSquareWave(valleyWidth, peakHeight, peakWidth, numberOfCycles)

turtle.Screen().exitonclick()
