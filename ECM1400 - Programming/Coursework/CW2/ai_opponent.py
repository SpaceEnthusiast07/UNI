"""..."""
import numpy as np


def calculate_move(board: list[list[str]]) -> tuple:
    """
    Takes in the current state of the board and calculates the number
    of opponent counters that are flipped as a result of each legal move.\n
    Then, it sorts this list in descending order of the number of flipped counters.\n
    To give the human player an advantage, choose the legal move that results in the\n
    second highest number of lipped counters, if 2 or more available moves are present.\n
    Otherwise, if there is only one legal move, choose this.\n
    Finally, if there are no legal moves, return (-1,-1), indicating no legal moves.
    """

    # Since the ai is the other opponent, colour = "Light"
    colour = "Light"
    # Calculate the size of the board
    size = len(board[0])
    # Initialise the list containing coord, number_of_flipped_counters pairs
    list_of_legal_moves = []

    # Loop through each cell in the board
    for row in range(size):
        for column in range(size):
            # If cell contains "None ", check if a legal move is possible
            if board[row, column] == "None ":
                result = legal_move(colour, (column, row), board)

                # Check if this cell results in a legal move
                if result[0] is True:
                    # Update the list of moves
                    list_of_legal_moves.append(((column+1, row+1), result[1]))

    # Sort list_of_legal_moves into descending order
    sorted_list_of_legal_moves = sorted(list_of_legal_moves, key=lambda x: x[1], reverse=True)

    # So that the human player has a chance, the AI will
    # always choose the second best place for the light counter
    if len(sorted_list_of_legal_moves) == 1:
        choosen_coordinate = sorted_list_of_legal_moves[0][0]
    elif len(sorted_list_of_legal_moves) > 1:
        choosen_coordinate = sorted_list_of_legal_moves[1][0]
    else:
        choosen_coordinate = (-1,-1)

    # Return whether the player can make a legal move
    return choosen_coordinate


def legal_move(colour: str, coordinate: tuple, board: list[list[str]]) -> tuple:
    """
    First checks if a counters is already present at the current coordinate.
    If true, this coordinate results in an illegal move.\n
    Then, loops through each direction to see if the AI can outflank its opponent.\n
    Returns a tuple containing a boolean representing if at least on direction is legal 
    and then the number of total counter flipped from all directions.
    """

    # To access a cell in a 2D array, the row index is provided before the column index
    # This means that the y-axis is provided before the x-axis
    # Wrong: board[xCoord, yCoord] = board[cell_to_check[0], cell_to_check[1]]
    # Right: board[yCoord, xCoord] = board[cell_to_check[1], cell_to_check[0]]

    # Calculate the size of the board
    size = len(board[0])
    # Array of directions
    directions = np.array([(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)])
    # Convert the coordinate to a numpy array
    coordinate = np.array(coordinate)
    # Initialise the legal_direction, representing if there exists a direction that is legal
    legal_direction = False
    # Initialise the number_of_flipped_counters, representing how many counters have been flipped
    number_of_flipped_counters = 0

    # First, lets check whether a counter is already present at this location
    if (board[coordinate[1], coordinate[0]] != "None "):
        return (False, 0)

    # Loop through each direction
    for direction in directions:
        # Compute the first cell to check
        cell_to_check = coordinate + direction

        # Ensure the first cell along the direction is within the board boundaries
        if (cell_to_check[0] >= 0 and cell_to_check[0] < size
            and cell_to_check[1] >= 0 and cell_to_check[1] < size):
            # Check if the cell contains "None ", if not,
            # a legal move is possible along this direction
            if board[cell_to_check[1], cell_to_check[0]] != "None ":
                # Analsye the first cell in this direction
                result = analyse_cell(colour, cell_to_check, board, direction, size)

                # Check if this direction has resulted in an outflank,
                # state so and increment the counter
                if result[0] is True:
                    legal_direction = True
                    # Increment the fippedCounters counter
                    number_of_flipped_counters += result[1]

    return (legal_direction, number_of_flipped_counters)


# Function to analyse a cell to determine if the player can outflank the other
def analyse_cell(colour: str, cell_to_check: tuple, board: list[list[str]],
                 direction: tuple, size: int) -> tuple:
    """
    Recursive function that travels along a direction to determine if it is legal.

    #### Base case:
         - If we have travelled beyong the board boundaries, the current direction must be illegal,
           therefore start backtracking through the recursion.
    
    #### Recursive case:
         - Check if current cell to check contains the AI's colour (`"Light"`), if `true`, the
           AI can outflank its opponent in this direction.
         - If the cell to check contains the value `"None "`, that means the AI cannot outflank its
           opponent in this direction.
         - Otherwise, step one cell further along this direction and repeat this process.
    """

    # Base Case: Check if we are outside the boundaries of the board
    if (cell_to_check[0] < 0 or cell_to_check[0] >= size
        or cell_to_check[1] < 0 or cell_to_check[1] >= size):
        # Since we have gone outside the boundaries of the board,
        # this direction must not contain any other counters
        return (False, 0)

    # Recursive Section:
    # Check if we have reached the players colour
    if (board[cell_to_check[1], cell_to_check[0]] == colour):
        return (True, 0)

    # Check if we have reached an empty cell
    if (board[cell_to_check[1], cell_to_check[0]] == "None "):
        return (False, 0)

    # Otherwise, we must have reached the other player's colour
    # Since this cell contains the other player's colour,
    # analyse the next cell along the current direction
    result = analyse_cell(colour, cell_to_check + direction, board, direction, size)
    # If result[0] == true, this direction is legal, return true
    if result[0] is True:
        return (True, 1)
    # Either direction is empty or player cannot outflank the other player in this direction
    return (False, 0)
