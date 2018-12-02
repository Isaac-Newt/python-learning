# Isaac List - November 2, 2018 - Lab 9 Part 3

import random
import turtle


def drawTriangles(turtles, sideLength) :

    for turtle in range(len(turtles)):
        for integer in range(3):
            turtles[turtle].forward(sideLength)
            turtles[turtle].left(120)


screen = turtle.Screen()

turtles = []

for turtleNumber in range(16) :

    newTurtle = turtle.Turtle()

    newTurtle.penup()
    newTurtle.goto(random.randrange(-150, 151), random.randrange(-150, 151))
    newTurtle.setheading(random.randrange(360))
    newTurtle.pendown()

    turtles.append(newTurtle)

drawTriangles(turtles, 50)

screen.exitonclick()
