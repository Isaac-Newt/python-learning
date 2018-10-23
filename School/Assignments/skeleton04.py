# Isaac List - CS150 - October 23, 2018
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
# Functions to deal with Inputs
#

# Integer input
def inputInt(prompt) :
    # Prompts for, reads, and returns an int value
    return int(input(prompt + ' (an int) '))

# Float input
def inputFloat(prompt) :
    # Prompts for, reads, and returns a float value
    return float(input(prompt + ' (a float) '))

#
# Functions to do during Setup
#

# Drawing the arena boundary
def drawArenaBoundary(arenaRadius) :
    # Draws a square of a given radius centered on world coordinate (0, 0)
    # showing the boundary of an arena

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

    return arena

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

    # return turtle names, which will be set to variables in main program body
    return turtleForPlayer1, turtleForPlayer2

#
# Functions to do During a turn
#

# Determine x-coordinates of turtle if move is made
def newXCoordinate(direction, distance, subjectTurtle) :
    # Returns the x-coordinate a subject turtle would be at if it were
    # to move in a given direction for a given distance
    return subjectTurtle.xcor() + distance * math.cos(math.radians(direction))

# Determine y-coordinates of turtle if move is made
def newYCoordinate(direction, distance, subjectTurtle) :
    # Returns the x-coordinate a subject turtle would be at if it were
    # to move in a given direction for a given distance
    return subjectTurtle.ycor() + distance * math.sin(math.radians(direction))

# Get arenaRadius input
def getArenaRadiusInput():
    # Get custom arena size from user
    arenaRadius = inputInt('Enter the radius of the arena: ')

    # If chosen value is invalid, ask again, keep asking until given good value
    while arenaRadius <= 0 :
        print('**** The arena radius must be > zero')
        arenaRadius = inputInt("Enter the radius of the arena: ")

    # Return arenaRadius to be used in main program body
    return arenaRadius

# Given a direction "candidate", returns True if invalid, False if valid
def isInvalidDirection(candidate):
    if candidate == "up" or candidate == "down" or candidate == "left" or candidate == "right":
        return False
    else:
        return True

#
# Get user inputs for the move, evaluate those inputs
#

#
# Get the user's inputs
#

# Direction (north/east/south/west)
def getUserDirection(playerTurtle):
    # Until user inputs a valid direction, keep asking
    direction = ""
    while isInvalidDirection(direction):
        direction = input("What direction should your turtle travel? left, right, up, or down: ")

    # Convert direction to a numerical heading, and set turtle's heading
    if direction == "right":
        playerTurtle.setheading(0)
        direction = 0
    elif direction == "up":
        playerTurtle.setheading(90)
        direction = 90
    elif direction == "left":
        playerTurtle.setheading(180)
        direction = 180
    elif direction == "down":
        playerTurtle.setheading(270)
        direction = 270

    # direction needs to be returned so it can be used in out of bounds function
    return direction

# Distance
def getUserDistance():
    distance = inputInt("How far should your turtle move?: ")
    return distance

#
# Functions that Evaluate the inputs and other conditions
#

# Decide if move will take turtle out of bounds
def moveWouldTakeTurtleOutOfArena(direction, distance, subject, radius):
    # Define the potential coordinates
    newXLocation = newXCoordinate(direction, distance, subject)
    newYLocation = newYCoordinate(direction, distance, subject)

    # Check potential coordinates, return if they are within arena or not
    if abs(newXLocation) > radius or abs(newYLocation) > radius:
        return False
    else:
        return True

# Decide if the player has won, based on distance between the turtles
def hasThePlayerWon(distanceExpression):
    if distanceExpression:
        victory = True
    else:
        victory = False

# Decide what message to print, based on whether someone has won the game
def printFinalMessage(victory):
    if victory:
        print("Congratulations player" + str(playerNumber) + "! You won!")
    else:
        print("The game is a draw.")

# Move the turtle the user-chosen distance
def moveTurtle(distance, subject):
    subject.forward(distance)

#
# Main function to run one turn
#

# Function to play one move, given the move number,
# arena size, and player details
def playOneMove(moveNumber, playerNumber, playerTurtle, arenaRadius):
    # Define which turtle to use, and which one is the opponent's
    if playerNumber == 1:
        playerTurtle = turtleForPlayer1
        opponentTurtle = turtleForPlayer2
    else:
        playerTurtle = turtleForPlayer2
        opponentTurtle = turtleForPlayer1

    # Print the current player
    print("It is player ", playerNumber, "'s turn")

    # Get user inputs

    # This will turn the turtle on its own
    direction = getUserDirection(playerTurtle)

    # This will set distance equal to the return value of getUserDistance()
    distanceToTravel = getUserDistance()

    # Check to see if within arena
    while not moveWouldTakeTurtleOutOfArena(direction, distanceToTravel, playerTurtle, arenaRadius):
        # Print a helpful message
        print("This will take your turtle out of bounds, please enter a new direction.")

        # run the usual inputs

        # This will turn the turtle on its own
        getUserDirection(playerTurtle)

        # This will set distance equal to the return value of getUserDistance()
        distanceToTravel = getUserDistance()

    # once given good distance/directions, move the turtle distanceToTravel
    moveTurtle(distanceToTravel, playerTurtle)

    # Check whether player has won
    #
    # Using the turtle.distance() function, determines the distance
    # between the player's turtle and their opponent's turtle
    hasThePlayerWon(playerTurtle.distance(opponentTurtle) <= winningDistanceUpperBound)
    if (playerTurtle.distance(opponentTurtle) <= winningDistanceUpperBound):
        victory = True
    else:
        victory = False

    # Switch the user, except if a player has won
    if victory:
        playerNumber = playerNumber
    elif playerNumber == 1:
        playerNumber = 2
    else:
        playerNumber = 1

    # Return playerNumber and victory, to determine next player, or if current player won
    return playerNumber, victory

#
# Actual program body.  No functions below here!
#

#
# Setup the game
#

# Get custom arena size from user
arenaRadius = getArenaRadiusInput()

# Set up Arena
arena = arenaSetup()

# Set up turtles
turtleForPlayer1, turtleForPlayer2 = turtlesSetup()

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

# Initialize necessary variables and conditions and such

# Run game for max of 20 turns, start count at 1
turn = 1

# No one has won yet, so victory == False
victory = False

# Start with pseudo-randomly chosen player, then alternates each turn
playerNumber = playerMakingMove

#
# Play the game!
#

# Run the game for a max of 20 turns for each player, or until someone wins.

# In boolean logic, run the game while both turn <=20 and (not victory) are True.
# If either are False (exceed moves, or someone wins) then the game is finished.

while turn <= (maximumNumberOfMoves * 2) and (not victory) :
    # Activate the correct turtle
    if playerNumber == 1:
        playerTurtle = turtleForPlayer1
    else:
        playerTurtle = turtleForPlayer2
    # Run the player's turn, will alternate the active player each time
    playerNumber, victory = playOneMove(turn, playerNumber, playerTurtle, arenaRadius)

    # incriment round counter
    turn += 1

# End of the game, so print a message
printFinalMessage(victory)

# Exit the window when clicked,
print('Click on the arena to end the game')
arena.exitonclick()
