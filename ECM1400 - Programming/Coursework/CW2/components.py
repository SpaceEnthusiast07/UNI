import numpy as np

# Function to set up the board
def initialise_board(size=8):
    # Check if the size is odd
    if (size % 2 == 1):
        print("Board cannot be an odd size.")
        return None
    
    # Board representation structure
    #   None = null/empty cell
    #   Dark = black counter in cell
    #   Light = white counter in cell

    # Create the 2d array representation of the board
    board = np.full(shape=(size,size), fill_value="None ")

    # Set up the four centre cells with the required pattern
    halfSize = size//2
    board[(halfSize) - 1, (halfSize) - 1] = "Light"
    board[(halfSize) - 1, halfSize] = "Dark "
    board[halfSize, (halfSize) - 1] = "Dark "
    board[halfSize, halfSize] = "Light"

    # Return the board
    return board


# Function to print a representation of the board to the console
def print_board(board):
    # Calculate the size of the board
    size = len(board[0])

    # Initialise a string to hold the row
    rowString = ""

    # Print key
    print("Key:\n  Empty = -\n  Dark = X\n  Light = O\n")
    # Print column numbers
    columnNumbers = "   "
    for i in range(1,size+1): columnNumbers += f"{i} "
    print(columnNumbers)

    # loop through each cell on the board
    for row in range(size):
        # Add row number to row string
        rowString += f" {row+1} "
        for column in range(size):
            if (board[row,column] == "None "): rowString += "- "
            elif (board[row,column] == "Dark "): rowString += "X "
            elif (board[row,column] == "Light"): rowString += "O "
        # Ouput the row
        print(rowString)
        # Reset the row string
        rowString = ""


# Function that determines if a move is legal or not
def legal_move(colour, coordinate, board):
    # Array of directions
    directions = np.array([(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)])
    # Convert the coordinate to a numpy array
    coordinate = np.array(coordinate) - 1
    # Initialise the legalDirection, representing if there exists a direction that is legal
    legalDirection = False
    
    # Loop through each direction
    for direction in directions:
        # Compute the first cell to check
        cellToCheck = coordinate + direction

        # Ensure the next cell along the direction is within the board boundaries
        if (cellToCheck[0] > 1 or cellToCheck[0] < size or cellToCheck[1] > 1 or cellToCheck[1] < size):
            # Check if the cell contains "None ", if not, a legal move is possible along this direction
            if (board[cellToCheck[0], cellToCheck[1]] != "None "):
                # Analsye the first cell in this direction
                result = analyse_cell(colour, cellToCheck, board, direction)
                # Check if this direction has resulted in an outflank
                if (result): 
                    legalDirection = True
                    board[coordinate[0], coordinate[1]] = colour
    
    # Check if any direction has resulted in a legal move
    return legalDirection


# Function to analyse a cell to determine if the player can outflank the other
def analyse_cell(colour, cellToCheck, board, direction):
    # Base Case: Check if we are at the end of the board
    if (cellToCheck[0] < 1 or cellToCheck[0] > size or cellToCheck[1] < 1 or cellToCheck[1] > size):
        # Since we are at the end of the board, this direction must not contain any other counters
        return False
    
    # Recursive Section:
    # Check if we have reached the players colour
    if (board[cellToCheck[0], cellToCheck[1]] == colour): return True

    # Check if we have reached an empty cell
    elif (board[cellToCheck[0], cellToCheck[1]] == "None "): return False

    # Check if we have reached the other player's colour
    else:
        # Since cell is other players colour, analyse next cell along direction
        result = analyse_cell(colour, cellToCheck+direction, board, direction)
        # If result is true, that means player has outflanked the other player along this direction
        if (result == True):
            # Therefore, change this cell to the player's colour
            board[cellToCheck[0], cellToCheck[1]] = colour
            return True
        else:
            # Either direction is empty or player cannot outflank the other player in this direction
            return False
        

import os

# Initialise the board
board = initialise_board()
# Calculate the size of the board
size = len(board[0])

i=0
while True:
    print("\n=== Revelio Game ===")
    # Display the current state of the board
    print_board(board)

    # Switch player turns
    if i % 2 == 0: colour = "Dark "
    else: colour = "Light"

    # Input the x-coord for the next move
    userCoordX = input(f"\nx coord for {colour}? ")
    if userCoordX == "q": break

    # Input the y-coord for the next move
    userCoordY = input("y coord for dark? ")

    # Check if this is a legal move
    print(f"The result of this move is: {legal_move(colour, (int(userCoordY), int(userCoordX)), board)}\n\n\n")
    i+=1

    # Clear the screen for the next player
    os.system("cls")