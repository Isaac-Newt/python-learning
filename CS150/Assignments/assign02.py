# Isaac List - CS150 September 19, 2018
#
# Assignment 2
#
# Draws a basic bar chart given lengths and colors.
# Includes a black border to make it look nice.

import turtle

# Define Turtle stuff
window = turtle.Screen()
john = turtle.Turtle()
john.pensize(5)

B = int(input("Enter a non-zero, positive integer: "))

# Set a variable to store the highest line height
highest = 0

# Colored Lines
for n in range(0, B):
    # Inputs
    H = int(input("Enter an integer length: "))
    C = input("Enter a color: ")
    
    # Compare current highest length with new "H", save highest value
    highest = max(highest, H)
    
    # Set Color
    john.color(C)
    # Position Turtle
    john.penup()
    john.forward(n*20)
    john.left(90)
    # Draw Line
    john.pendown()
    john.forward(H)
    # Go back to start
    john.penup()
    john.goto(0, 0)
    john.right(90)

# Black Border

# Define the width
width = B * 20

# Move turtle into position, change color to black
john.penup()
john.goto(-20, -20)
john.color("black")
john.pendown()

# Draw the box
for n in range(0,2):
    # width is B * 20 units, need extra 20 for area to left of lines
    john.forward(width + 20)
    john.left(90)
    # Height of tallest line, + 2*20 unit buffers
    john.forward(highest + 40)
    john.left(90)

window.exitonclick()
