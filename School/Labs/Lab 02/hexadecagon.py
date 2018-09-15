#
# This program uses turtle graphics to draw a hexadecagon
# Isaac List - CS150, 09-14-2018, Lab 3a
#

import turtle

canvas = turtle.Screen()

Frank = turtle.Turtle()
Frank.pensize(5)
Frank.forward(30) # Draws initial side

# Draw the other 15 sides
for i in range(0, 15, 1):
    Frank.left(22.5)
    Frank.forward(30)

canvas.exitonclick()
