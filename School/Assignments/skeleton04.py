# Isaac List - CS150 - October 19, 2018
#
# Assignment 4 - Turtle War Game

# This program is a game played by two players moving a turtle around
# the screen.  The game ends when either a) 20 moves have passed
# or b) when one player moves their turtle on top of the other

# Import necessary modules
import turtle
import math
import random

#
# Define various general function
#

# Inputs

# Integer input
def inputInt(prompt) :
    """Prompts for, reads, and returns an int value"""
    return int(input(prompt + ' (an int) '))

# Float input
def inputFloat(prompt) :
    """Prompts for, reads, and returns a float value"""
    return float(input(prompt + ' (a float) '))

# Setup

# Drawing the arena boundary
def drawArenaBoundary(arenaRadius) :
    """Draws a square of a given radius centered on world coordinate (0, 0) showing the boundary of an arena"""

    turtleForDrawingArenaBorder = turtle.Turtle()

    turtleForDrawingArenaBorder.speed(0)
    turtleForDrawingArenaBorder.pensize(5)
    turtleForDrawingArenaBorder.pencolor('red')

    turtleForDrawingArenaBorder.penup()
    turtleForDrawingArenaBorder.goto(- arenaRadius, arenaRadius)
    turtleForDrawingArenaBorder.pendown();

    for sideNumber in range(4) :
        turtleForDrawingArenaBorder.forward(2 * arenaRadius);
        turtleForDrawingArenaBorder.right(90);

    turtleForDrawingArenaBorder.hideturtle()

# Set up arena
def arenaSetup():
    # Create and initialize the screen holding the arena
    arena = turtle.Screen()

    # (Initialize)
    arena.title('Turtle War')
    arena.setup(50 + 2 * arenaRadius + 1, 50 + 2 * arenaRadius + 1)

    # Draw the boundary around the arena
    drawArenaBoundary(arenaRadius)

# Turtles Setup

def turtlesSetup():
    # Create Player 1's turtle
    turtleForPlayer1 = turtle.Turtle()
    turtleForPlayer1.shape('square')
    turtleForPlayer1.penup()

    # Create Player 2's turtle
    turtleForPlayer2 = turtle.Turtle()
    turtleForPlayer2.shape('triangle')
    turtleForPlayer2.penup()

    # Position both players' turtles at pseudo-randomly chosen positions in the arena
    turtleForPlayer1.goto(
        random.randrange(- arenaRadius, arenaRadius + 1),
        random.randrange(- arenaRadius, arenaRadius + 1)
        )

    turtleForPlayer2.goto(
        random.randrange(- arenaRadius, arenaRadius + 1),
        random.randrange(- arenaRadius, arenaRadius + 1)
        )

# During a turn

# Determine x-coordinates of turtle if move is made
def newXCoordinate(direction, distance, subjectTurtle) :
    """Returns the x-coordinate a subject turtle would be at if it were to move in a given direction for a given distance"""
    return subjectTurtle.xcor() + distance * math.cos(math.radians(direction))

# Determine y-coordinates of turtle if move is made
def newYCoordinate(direction, distance, subjectTurtle) :
    """Returns the x-coordinate a subject turtle would be at if it were to move in a given direction for a given distance"""
    return subjectTurtle.ycor() + distance * math.sin(math.radians(direction))

"""                      """
"""Below are MY functions"""
"""                      """

# Given a direction "candidate", returns True if invalid, False if valid
def isInvalidDirection(candidate):
    if candidate == "north" or candidate == "east" or candidate == "south" or candidate == "west":
        return False
    else:
        return True

#
# Get user inputs for the move
#

# Direction (north/east/south/west)
def getUserDirection():
    # Until user inputs a valid direction, keep asking
    direction = ""
    while isInvalidDirection(direction):
        direction = input("What direction should your turtle travel? (east, west, north, or south\)")

    # Convert direction to a numerical heading
    if direction == "east":
        playerTurtle.setheading(0)
    elif direction == "north":
        playerTurtle.setheading(90)
    elif direction == "west":
        playerTurtle.setheading(180)
    elif direction == "south":
        playerTurtle.setheading(270)

# Distance
def getUserDistance():
    distance = inputInt("How far should your turtle move?: ") # still in Turtle units!!!
    return distance

# Decide if move will take turtle out of bounds
def moveWouldTakeTurtleOutOfArena(direction, distance, subject, radius):
    pass

# Function to play one move, given the move number,
# arena size, and player details
def playOneMove(moveNumber, playerNumber, playerTurtle, arenaRadius):
    pass

#
# Actual program body.  No functions below here!
#

# Get custom arena size from user
arenaRadius = inputInt('Enter the radius of the arena: ')

if arenaRadius <= 0 :
    print('**** The arena radius must be > zero')
else :
    # Set up Arena
    arenaSetup()

    # Set up turtles
    turtlesSetup()
    
    # Pseudo-randomly decide which player moves first
    playerMakingMove = random.randrange(1, 3)

    # Let winningDistanceUpperBound be the maximum distance between the centers of two
    # turtles that still constitutes one turtle being positioned over another turtle
    winningDistanceUpperBound = 20

    # Let maximumNumberOfMoves be the maximum number of moves a game can go before the
    # game is considered to be a draw
    maximumNumberOfMoves = 20

    # Remind the players which turtle belongs to which player
    print('Player 1 is the square;  player 2 is the triangle')

    #
    # THE CODE FOR THE REST OF THE MAIN PROGRAM SHOULD GO BELOW THIS BLOCK OF COMMENTS
    #

    # Run game for 20 rounds, or until a player wins
    round = 1
    while round <= 20 or victory :
        playerNumber = playerMakingMove
        #
        # This will go in playOneMove() function
        #

        # Get user inputs
        getUserDirection()
        getUserDistance()

        # Check to see if within arena
        # Yeah, this'll take some math stuff :|

        # Switch the user
        if playerNumber == 1:
            playerNumber == 2
        else:
            playerNumber == 1


    #
    # THE CODE FOR THE REST OF THE MAIN PROGRAM SHOULD GO ABOVE THIS BLOCK OF COMMENTS
    #

    print('Click on the arena to end the game')
    arena.exitonclick()
