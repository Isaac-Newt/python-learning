# Isaac List  - CS150, 09-09-2018
#
# This program allows for user input on drawing a triangleself.
#
# Originally taken from https://runestone.academy text
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import turtle

bcolor = input("Select a Background color")
tcolor = input("Select a Line color")
size = int(input("Select a width"))

wn = turtle.Screen()
wn.bgcolor(bcolor)        # set the window background color

tess = turtle.Turtle()
tess.color(tcolor)              # make tess blue
tess.pensize(size)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
