from random import randint

# Create "board" list
board = []

# Create board layout
for x in range(0,5):
    board.append(["0"] * 5)

# Prints the board
def print_board(board):
    for row in board:
        print(" ").join(row)

print_board(board)

# Choose random row
def random_row(board):
    return randint(0, len(board) - 1)
# Choose random column
def random_col(board):
    return randint(0, len(board) - 1)

# Choose random grid plot
ship_row = random_row(board)
ship_col = random_col(board)
# only for debugging
# print(ship_row)
# print(ship_col)

# Take user guess
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Column: "))

# Give user 4 turns
for turn in range(4):
    print("Turn", turn + 1)
    # Do after guess
    if guess_row == ship_row and guess_col == ship_col:
        print("Contratulations! You sank the Battleship!")
        break
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
        print("You missed the battleship.")
        # Put "X" in guessed spot
        board[guess_row][guess_col] = "X"
        # If out of grid
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, thta's not in the ocean")
        else:
            print("You missed the battleship.")
            # Put "X" in guessed spot
            board[guess_row][guess_col] = "X"
        print_board(board)
    if turn == 3:
        print("Game Over")
