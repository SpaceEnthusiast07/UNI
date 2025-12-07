import numpy as np

def makeMove(board):
    # Since the ai is the other opponent, colour = "Light"
    colour = "Light"
    # Initialise legalMove
    legalMove = False
    # Initialise the list containing coord, flippedCounters pairs
    listOfMoves = []

    for row in range(len(board[0])):
        for column in range(len(board[0])):
            # If cell contains "None ", check if a legal move is possible
            if (board[row, column] == "None "):
                isLegalCell = legal_move(colour, (column, row), board, False)
            
                # If cell is legal
                if (isLegalCell[0]):
                    # Set legalMove to True
                    legalMove = True
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


def legal_move(colour, coordinate, board, modifyBoard):
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
    if (board[coordinate[1], coordinate[0]] != "None "): return (False, -1)
    
    # Loop through each direction
    for direction in directions:
        # Compute the first cell to check
        cellToCheck = coordinate + direction

        # Ensure the first cell along the direction is within the board boundaries
        if ((cellToCheck[0] >= 0) and (cellToCheck[0] < size) and (cellToCheck[1] >= 0) and (cellToCheck[1] < size)):
            # Check if the cell contains "None ", if not, a legal move is possible along this direction
            if (board[cellToCheck[1], cellToCheck[0]] != "None "):
                # Analsye the first cell in this direction
                result = analyse_cell(colour, cellToCheck, board, direction, size, modifyBoard)
                # Check if this direction has resulted in an outflank, and we are allowed to modify the board
                if (result[0] and modifyBoard): 
                    legalDirection = True
                    board[coordinate[1], coordinate[0]] = colour
                # If we are not allowed to modify the board, but the direction is legal, set legalDirection to true
                elif (result[0] == True and modifyBoard == False): 
                    legalDirection = True
                    # Increment the fippedCounters counter
                    flippedCounters += result[1]

    
    # Check if any direction has resulted in a legal move
    return (legalDirection, flippedCounters)


# Function to analyse a cell to determine if the player can outflank the other
def analyse_cell(colour, cellToCheck, board, direction, size, modifyBoard):
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
        result = analyse_cell(colour, cellToCheck + direction, board, direction, size, modifyBoard)
        # If result[0] is true, that means player has outflanked the other player along this direction
        if (result[0] and modifyBoard):
            # Therefore, change this cell to the player's colour
            board[cellToCheck[1], cellToCheck[0]] = colour
            return (True, 1)
        # If we are not allowed to modify the board, but this direction is still legal, return true
        elif (result[0] == True and modifyBoard == False): return (True, 1)
        else:
            # Either direction is empty or player cannot outflank the other player in this direction
            return (False, 0)
