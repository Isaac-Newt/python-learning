#
# Isaac List - CS150 09-14-2018 Lab 3c
# This program draws a shape based on user input
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import turtle

canvas = turtle.Screen()

Jane = turtle.Turtle()
Jane.pensize(3)
Jane.pencolor("orange")

# Get an integer for number of sides
n = int(input("Enter an integer: "))

for i in range(0, n, 1):
    # Get float values for length and angle to turn
    j = float(input("Enter a length: "))
    k = float(input("Enter an angle: "))

    # Draw line with j length and then turn k degrees
    Jane.forward(j)
    Jane.left(k)

print("Click on the drawing to exit")
canvas.exitonclick()
