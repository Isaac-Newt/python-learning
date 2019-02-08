#
# Isaac List - CS150 - October 3, 2018 - Lab 5
#
# This program prints a simple bar chart
#

import turtle


def inputInt(prompt) :

    value = input(prompt + '(an int) ')
    value = int(value)

    return value


def drawBar(turtleToDrawBar, lengthOfBar) :
    # Green if positive, purple if 0, red if negative
    if lengthOfBar > 0: 
        turtleToDrawBar.color("green")
    elif lengthOfBar == 0:
        turtleToDrawBar.color("purple")
    else:
        turtleToDrawBar.color("red")
    
    turtleToDrawBar.left(90)

    turtleToDrawBar.pendown()
    turtleToDrawBar.forward(lengthOfBar)
    turtleToDrawBar.penup()

    turtleToDrawBar.left(180)

    turtleToDrawBar.forward(lengthOfBar)

    turtleToDrawBar.left(90)


#
# Set the sizes for the components of the chart
#

barThickness = 10
distanceBetweenBars = 20

#
# Let pen be the turtle that will draw the bars
#

pen = turtle.Turtle()

#
# Intialize the pen's thickness and position
#

pen.pensize(barThickness)
pen.penup()

#
# Let numberOfBars be the number of bars to draw (read from input)
#

numberOfBars = inputInt('How many bars would you like? ')

#
# Draw the bars in the chart
#

for barNumber in range(numberOfBars) :

    #
    # Let barHeight be the height of the next bar (read from input)
    #

    barHeight = inputInt('How tall is the next bar? ')

    #
    # Draw the bar, spaced from any adjacent bars
    #

    pen.forward(distanceBetweenBars / 2)

    drawBar(pen, barHeight)

    pen.forward(distanceBetweenBars / 2)

#
# Halt the program when the user clicks on the drawn graph
#

turtle.Screen().exitonclick()
