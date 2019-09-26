from random import randint

# Create "board" list
board = []

# Create board layout
for x in range(5):
    board.append(["0"] * 5)
    
# Prints the board
def print_board(board):
    for row in board:
        print " ".join(row)
        
# Begin the game
print "Let's play Battleship!"
print_board(board)

# Choose random row/col
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

# Assign hiding spot for ship
ship_row = random_row(board)
ship_col = random_col(board)

# To be used for debugging
# print ship_row
# print ship_col

# Guessing Sequence begins
# User gets 4 turns
for turn in range(4):
    print "Turn", turn + 1
    
    # Prompt for guesses
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    
    # Do after guess
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not in the ocean!"
        elif (board[guess_row][guess_col] == "X"):
            print "You already guessed that one!"
        else:
            print "You missed my battleship!"
            # Put "X" on guessed spot
            board[guess_row][guess_col] = "X"
            
        print_board(board)
        
    if turn == 3:
        print "Game Over"
        break
