"""
This module contains three utility functions that provide the
functionality for the Othello/Reversi game to work.

Typlical import:
  >>> import components as comp

Public Functions:
 - initialise_board()
 - print_board()
 - legal_move()

Internal Helper Functions:
 - _analyse_cell()

### Brief Function Description
#### 1. initialise_board(size: int = 8):
Creates a Reversi/Othello board of default size 8x8.

Sets up the centre four counters as follows:
    |Light|Dark |
    |Dark |Light|

If board is an odd size, e.g. `size=9`, `None` is returned.

Example:
  >>> board = comp.initialise_board(size=6)


#### 2. print_board(board: list[list[str]]):
Prints a representation of the `board` to the console.

A *key* is displayed before the board to indicate what each symbol means.

Column and row numbers are displayed to make the process of reading the board easier.

Example:
  >>> comp.print_board(board)


#### 3. legal_move(colour: str, coordinate: tuple, board: list[list[str]], modify_board: bool):
Given a player's `colour`, chosen `coordinate`, the current state of the `board` and
whether the board should be *modified* or not, determine whether this move is legal,
based on the rules of Othello/Reversi.

Example:
  >>> legal_move_result = comp.legal_move("Light", (6,7), board, True)
>>> # Check if (6,7) is a legal move for player "Light"
>>> if legal_move_result['is_legal_move'] is True:
>>>     # Extract the new state of the board, only required if modify_board=True
>>>     board = legal_move_result['board']
"""

from numpy import full
from numpy import array


def initialise_board(size: int = 8) -> list[list[str]]:
    """
    Optionally pass in the preferred `size` of the board, default is `8`.

    Returns `None` if the preferred size is odd.

    Uses the `numpy.full()` function to create an array of `shape=(size,size)` and
    `fill_value="None "`. This sets the default value for each cell to `"None "`,
    indicating that it is an empty cell.

    Then, it sets up the four centre cells in the following pattern:
        |Light|Dark |
        |Dark |Light|

    Finally, the function converts the `numpy` array object into a regular
    python 2d list and returns this new board.
    """

    # Check if the size is odd
    if size % 2 == 1:
        return None

    # Board representation structure
    #   None = null/empty cell
    #   Dark = black counter in cell
    #   Light = white counter in cell

    # Create the 2d array representation of the board
    board = full(shape=(size,size), fill_value="None ")

    # Set up the four centre cells with the required pattern
    half_of_size = size//2
    board[(half_of_size) - 1, (half_of_size) - 1] = "Light"
    board[(half_of_size) - 1, half_of_size] = "Dark "
    board[half_of_size, (half_of_size) - 1] = "Dark "
    board[half_of_size, half_of_size] = "Light"

    # Return the board
    return board.tolist()


def print_board(board: list[list[str]]):
    """
    Prints a representation of the `board` to the console.

    A key is displayed before the board to indicate what each symbol means.

    Column and row numbers are displayed to make the process of reading the board easier.

    Printing is optimised for a board of `size` less than 10. 
    This will be improved in a future update.
    """

    # Calculate the size of the board
    size = len(board[0])
    # Initialise a string to hold the row
    string_representation_of_row = ""

    # Print key and column numbers
    print("Key:\n  Empty = -\n  Dark = X\n  Light = O\n   " + " ".join(range(1, size+1)))

    # loop through each cell on the board
    for row in range(size):
        # Add row number to row string
        string_representation_of_row += f" {row+1} "
        for column in range(size):
            if board[row][column] == "None ":
                string_representation_of_row += "- "
            elif board[row][column] == "Dark ":
                string_representation_of_row += "X "
            elif board[row][column] == "Light":
                string_representation_of_row += "O "

        # Ouput the row
        print(string_representation_of_row)
        # Clear the row string
        string_representation_of_row = ""


def legal_move(colour: str, coordinate: tuple, board: list[list[str]], modify_board: bool) -> dict:
    """
    Pass in the current player's `colour`, chosen `coordinate`, the
    current state of the `board` and whether you want to `modify_board` or not.

    First checks whether this chosen cell is empty, if true, returns the
    dictionary indicating that this move is illegal.

    Initialises a `numpy.array()` of vector directions.

    Then it loops through each direction, calculating the first cell along this
    direction and checking that it is within the boundaries of the board.

    Ensuring this `cell_to_check` contains a counter ("Light" or "Dark ").

    It uses the `_analyse_cell()` recursive helper function to travel along the current direction
    to determine if the `colour` can outflank the other.

    Returns the dictionary representing if the move is legal and the new state of board.
    """

    # To access a cell in a 2D array, the row index is provided before the column index
    # This means that the y-axis is provided before the x-axis
    # Wrong: board[xCoord, yCoord] = board[cell_to_check[0], cell_to_check[1]]
    # Right: board[yCoord, xCoord] = board[cell_to_check[1], cell_to_check[0]]

    # Convert the board to a numpy array
    board = array(board)
    # Calculate the size of the board
    size = len(board[0])
    # Array of directions
    directions = array([(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)])
    # Convert the coordinate to a numpy array
    coordinate = array(coordinate) - array((1,1))
    # Initialise the is_legal_direction, representing if there exists a direction that is legal
    is_legal_direction = False

    # First, lets check whether a counter is already present at this location
    if board[coordinate[1], coordinate[0]] != "None ":
        return {
            'is_legal_move': False,
            'board': board.tolist()
        }

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
                result = _analyse_cell(colour, cell_to_check, board, direction, modify_board)
                # Check if this direction has resulted in an outflank,
                # and we are allowed to modify the board
                if result is True and modify_board is True:
                    is_legal_direction = True
                    board[coordinate[1], coordinate[0]] = colour
                # If we are not allowed to modify the board,but the direction is legal,
                # set is_legal_direction to true
                elif result is True and modify_board is False:
                    is_legal_direction = True

    return {
        'is_legal_move': is_legal_direction,
        'board': board.tolist()
    }


def _analyse_cell(colour: str, cell_to_check: object, board: object,
                 direction: object, modify_board: bool) -> bool:
    """
    Recursive function that travels along a `direction` to determine if it is a legal direction.

    Returns `True` if this direction results in an outflank, otherwise it returns `False`.
    """

    # Calculate the size of the board
    size = len(board[0])

    # Base Case: Check if we are outside the boundaries of the board
    if (cell_to_check[0] < 0 or cell_to_check[0] >= size
        or cell_to_check[1] < 0 or cell_to_check[1] >= size):

        # Since we have gone outside the boundaries of the board,
        # this direction must not contain any other counters
        return False

    # Recursive Section:
    # Check if we have reached the players colour
    if board[cell_to_check[1], cell_to_check[0]] == colour:
        return True

    # Check if we have reached an empty cell
    if board[cell_to_check[1], cell_to_check[0]] == "None ":
        return False

    # Otherwise, we must have reached the other player's colour
    # Since this cell contains the other player's colour,
    # analyse the next cell along the current direction
    result = _analyse_cell(colour, cell_to_check + direction, board, direction, modify_board)
    # If result is true, that means player has outflanked the other player along this direction
    if result is True and modify_board is True:
        # Therefore, change this cell to the player's colour
        board[cell_to_check[1], cell_to_check[0]] = colour
        return True
    # If we are not allowed to modify the board, but this direction is still legal, return true
    if result is True and modify_board is False:
        return True
    # Either direction is empty or player cannot outflank the other player in this direction
    return False
