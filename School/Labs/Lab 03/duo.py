#
# This program uses two turtles to draw two squares, with turtles 
# drawing in opposite directions, taking turns drawing sides.
# 
# Isaac List - CS150, 09-14-2018 Lab 3b
#

import turtle

canvas = turtle.Screen()

# Set up green turtle
green = turtle.Turtle()
green.pencolor("green")
green.pensize(5)

# Set up purple turtle
purple = turtle.Turtle()
purple.pencolor("purple")
purple.pensize(5)

# move purple into position
purple.penup()
purple.forward(25)
purple.pendown()

# orient green
green.left(180)

# Green draws clockwise, purple counter-clockwise
for sideNumber in [ 1, 2, 3, 4 ] :
    green.forward(50)
    green.right(90)
    purple.forward(50)
    purple.left(90)   

canvas.exitonclick()
