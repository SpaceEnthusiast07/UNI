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
    board[(size//2) - 1, (size//2) - 1] = "Light"
    board[(size//2) - 1, size//2] = "Dark "
    board[size//2, (size//2) - 1] = "Dark "
    board[size//2, size//2] = "Light"

    # Return the board
    return board


# Function to print a representation of the board to the console
def print_board(board):
    # Calculate the size of the board
    size = len(board[0])

    # Initialise a string to hold the row
    rowString = ""

    # Print key
    print("Key:\n  Empty = -\n  Dark = •\n  Light = ◦\n")

    # loop through each cell on the board
    for row in range(size):
        for column in range(size):
            if (board[row,column] == "None "): rowString += "- "
            elif (board[row,column] == "Dark "): rowString += "• "
            elif (board[row,column] == "Light"): rowString += "◦ "
        # Ouput the row
        print(rowString)
        # Reset the row string
        rowString = ""


# Function that determines if a move is legal or not
def legal_move(colour, coordinate, board):
    # Loop through each direction
    for i in range(8):
        if (i % 2 == 0):
            vert = 1
            hori = 0



board = initialise_board()
print_board(board)