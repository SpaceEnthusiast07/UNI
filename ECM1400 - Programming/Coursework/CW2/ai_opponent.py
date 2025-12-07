import numpy as np

def numberOfFreeCells(board):
    freeCellCounter = 0
    for row in range(len(board[0])):
        for column in range(len(board[0])):
            if (board[row, column] == "None "): 
                coord = (column+1, row+1)
                freeCellCounter += 1
    return (freeCellCounter, coord)


def makeMove(board):
    # Since the ai is the other opponent, colour = "Light"
    colour = "Light"
    # Calculate the size of the board
    size = len(board[0])
    # Initialise the list containing coord, flippedCounters pairs
    listOfMoves = []

    # Determine how many free cells there are
    freeCells = numberOfFreeCells(board)
    if (freeCells[0] == 1):
        # Automatically place the light counter here
        return freeCells[1]

    for row in range(size):
        for column in range(size):
            # If cell contains "None ", check if a legal move is possible
            if (board[row, column] == "None "):
                isLegalCell = legal_move(colour, (column, row), board)
            
                # If cell is legal
                if (isLegalCell[0]):
                    # Update the list of moves
                    listOfMoves.append(((column+1, row+1), isLegalCell[1]))
    
    # Sort listOfMoves into descending order
    listOfMoves_sorted = sorted(listOfMoves, key=lambda x: x[1], reverse=True)

    # So that the human player has a chance, i will always choose the second best place for the light counter
    if (len(listOfMoves_sorted) >= 2):
        bestCoord = listOfMoves_sorted[1][0]
    elif (len(listOfMoves_sorted) == 0):
        bestCoord = (-1,-1)
    else:
        bestCoord = listOfMoves_sorted[0][0]
    
    # Return whether the player can make a legal move
    return bestCoord


def legal_move(colour, coordinate, board):
    # To access a cell in a 2D array, the row index is provided before the column index
    # This means that the y-axis is provided before the x-axis
    # Wrong: board[xCoord, yCoord] = board[cellToCheck[0], cellToCheck[1]]
    # Right: board[yCoord, xCoord] = board[cellToCheck[1], cellToCheck[0]]

    # Calculate the size of the board
    size = len(board[0])
    # Array of directions
    directions = np.array([(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)])
    # Convert the coordinate to a numpy array
    coordinate = np.array(coordinate)
    # Initialise the legalDirection, representing if there exists a direction that is legal
    legalDirection = False
    # Initialise the flippedCounters, representing how many counters have been flipped
    flippedCounters = 0

    # First, lets check whether a counter is already present at this location
    if (board[coordinate[1], coordinate[0]] != "None "): return (False, 0)
    
    # Loop through each direction
    for direction in directions:
        # Compute the first cell to check
        cellToCheck = coordinate + direction

        # Ensure the first cell along the direction is within the board boundaries
        if ((cellToCheck[0] >= 0) and (cellToCheck[0] < size) and (cellToCheck[1] >= 0) and (cellToCheck[1] < size)):
            # Check if the cell contains "None ", if not, a legal move is possible along this direction
            if (board[cellToCheck[1], cellToCheck[0]] != "None "):
                # Analsye the first cell in this direction
                result = analyse_cell(colour, cellToCheck, board, direction, size)

                # Check if this direction has resulted in an outflank, state so and incremt the counter
                if (result[0] == True): 
                    legalDirection = True
                    # Increment the fippedCounters counter
                    flippedCounters += result[1]
    
    return (legalDirection, flippedCounters)


# Function to analyse a cell to determine if the player can outflank the other
def analyse_cell(colour, cellToCheck, board, direction, size):
    # Base Case: Check if we are outside the boundaries of the board
    if (cellToCheck[0] < 0 or cellToCheck[0] >= size or cellToCheck[1] < 0 or cellToCheck[1] >= size):
        # Since we have gone outside the boundaries of the board, this direction must not contain any other counters
        return (False, 0)
    
    # Recursive Section:
    # Check if we have reached the players colour
    if (board[cellToCheck[1], cellToCheck[0]] == colour): return (True, 0)

    # Check if we have reached an empty cell
    elif (board[cellToCheck[1], cellToCheck[0]] == "None "): return (False, 0)

    # Otherwise, we must have reached the other player's colour
    else:
        # Since this cell contains the other player's colour, analyse the next cell along the current direction
        result = analyse_cell(colour, cellToCheck + direction, board, direction, size)
        # If result[0] == true, this direction is legal, return true
        if (result[0] == True): return (True, 1)
        # Either direction is empty or player cannot outflank the other player in this direction
        else: return (False, 0)
