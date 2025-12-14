"""
This module is used to host the Othello game within the command line interface.

Typical Import:
  >>> import game_engine

Public Functions:
 - simple_game_loop()

Private Helper Functions:
 - _cli_coords_input()
 - _any_legal_moves()


### Brief Function Description
#### 1. simple_game_loop():
This is the main function for the command line implementation of Othello/Reversi.

It deals with the logic behind verifying a move and ensuring the game can continue.

Once the game has ended, it calculates who is the winner, or if it is a draw, then
displayes the winner with the scores for each player.

Example Usage:
  >>> # Run the game
>>> game_engine.simple_game_loop()


#### 2. _cli_coords_input():
This function aims to ask the current player for their chosen coordinates and contains
a loop for re-entering coordinates if they are invalid.


#### 3. _any_legal_moves(colour: str, board: object):
The purpose of this function is to determine if the specified colour player
has at least one legal move available, if so returns True, otherwise returns False.
"""

import os
import platform
import time
import components as comp


def _cli_coords_input() -> tuple[int, int]:
    """
    Uses the command line interface and requests the user to
    input their chosen `x` and `y` coordinates.

    Contains a loop, so if the user inputs invalid coordinates, the function
    asks them to input their chosen coordinates again.
    """

    valid_coordinates = False
    while valid_coordinates is False:
        # Ask the user for the x and y coordinate
        user_x_input = input("Enter x-coord: ")
        user_y_input = input("Enter y-coord: ")

        # Check if they have inputted an integer for x and y
        try:
            # Convert both coordinates to integers
            x_coord = int(user_x_input)
            y_coord = int(user_y_input)

            valid_coordinates = True
        except ValueError:
            # Inform the user that these are invalid coordinates
            print("Invalid coordinates!")

    # Format and return the coordinate tuple
    return (x_coord, y_coord)


def _any_legal_moves(colour: str, board: object) -> bool:
    """
    Searches through the board and for each empty cell, determines if
    this is a legal move for the specified colour player.

    True is returned if one legal move is found, otherwise False is returned.
    """

    for row in range(len(board[0])):
        for column in range(len(board[0])):
            # If cell contains "None ", check if a legal
            if (board[row, column] == "None "):
                is_legal_cell_results = comp.legal_move(colour, (column, row), board, False)

                # If cell is legal, return True
                if is_legal_cell_results['is_legal_move_results'] is True:
                    return True

    return False


def simple_game_loop():
    """
    This is the main loop for the command line version of Othello/Reversi.

    Continues to loop until there are no moves left or neither player can make a legal move.

    At the start of each loop iteration, the command line screen is cleared for a consistent
    and non cluttered display of the game.

    The current board is displayed for the player's to see. Then the players are told who's
    turn it is and asks them to input their chosen x and y coordinates.

    If the move is legal, they are informed and after a certain amount of time, the loop continues,
    refreshing the screen and showing the new state of the board.

    If the move is not legal, the player is informed and asked to input their
    chosen coordinates again.

    When the board is full or neither player can make a legal move, the main loop exits,
    displaying who won and each player's score.
    """

    # Initialise the board
    board = comp.initialise_board()

    # Initialise the move counters
    move_counter = 60
    #light_counter = 0
    #dark_counter = 0

    # Initialise global game over tracker
    game_over = False

    # Initialise legal_move_possible and noLegalmove_counter
    legal_move_possible = True

    # Set the starting player
    current_player = "Dark "

    # Loop through each player's turn
    while legal_move_possible and move_counter > 0:
        # Check which os this python file is on and clear the screen
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

        # Display welcome message
        print("=== Welcome to Reversi ===")

        # Display the board
        comp.print_board(board)

        # If game is over, exit loop
        if game_over is True:
            break

        # Check if there are any moves left
        if move_counter == 0:
            game_over = True
            break

        # Check if there are any legal moves available for the current player
        if _any_legal_moves(current_player, board) is False:
            # Determine the other player
            if current_player == "Dark ":
                other_player = "Light"
            else:
                other_player = "Dark "

            # Check whether either player can make a move
            if _any_legal_moves(other_player, board) is False:
                # Therefore, game is over
                # Initialise player score counters
                light_counter = 0
                dark_counter = 0

                # Calculate the number of counters for each player
                for row in board:
                    for cell in row:
                        if cell == "Dark ":
                            dark_counter += 1
                        elif cell == "Light":
                            light_counter += 1

                game_over = True
                # Break out of game loop
                break

            # Switch to other player
            if current_player == "Dark ":
                # Inform the player that they have no legal moves
                print(current_player + "has no legal moves!")
                current_player = "Light"
            else:
                # Inform the player that they have no legal moves
                print(current_player + " has no legal moves!")
                current_player = "Dark "

            # Continue to next loop
            continue

        # Initialise legal_move_made
        legal_move_made = False

        print("-"*(len(board[0]) * 2 + 3))
        # Display which player's turn it is
        if current_player == "Dark ":
            print(f"{current_player[:4]}'s turn")
        else:
            print(f"{current_player}'s turn")

        # Allow the current player to keep placing counters until a legal move is made
        while legal_move_made is False:
            # Obtain the coordinates the current player is going to play
            coords = _cli_coords_input()

            # Check whether the move is legal
            is_legal_move_results = comp.legal_move(current_player, coords, board, True)
            if not is_legal_move_results['is_legal_move']:
                # Inform the player that this is not a legal move
                print("Not a legal move!\n")
                continue

            # Set legal_move_made to True
            legal_move_made = True

        other_player_counter = 0
        # Determine the other player
        if current_player == "Dark ":
            other_player = "Light"
        else:
            other_player = "Dark "

        # Initialise player score counters
        light_counter = 0
        dark_counter = 0
        # Calculate the number of counters for the other player
        for row in board:
            for cell in row:
                if cell == other_player:
                    other_player_counter += 1
                if cell == "Dark ":
                    dark_counter += 1
                if cell == "Light":
                    light_counter += 1

        # If no of the other player's counters are present, game is over
        if other_player_counter == 0:
            game_over = True
            continue

        # Switch to other player
        if current_player == "Dark ":
            current_player = "Light"
        else:
            current_player = "Dark "

        # Decrement the move counter
        move_counter -= 1

        # Output legal move
        print("\nMove is legal!")
        time.sleep(2)

    # Print game over message and who won along with the counter stats
    print("\n-- GAME OVER --")
    # Check who won
    if dark_counter > light_counter:
        print("Dark Won!")
    else:
        print("Light Won!")

    # Output the points scored by each player
    print(f"\nScores:\n  -> Dark scored {dark_counter} \n  -> light scored {light_counter}")


# Only runs simple_game_loop automatically if this file is being run directly
# This ensures that when this module is imported, simple_game_loop does not run automatically
if __name__ == "__main__":
    simple_game_loop()
