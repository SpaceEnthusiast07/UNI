"""
This module is used to host the Othello game using Flask (a python web server and framework)
and website GUI.

To use your own website GUI, replace the default `index.html` file within the `templates`
folder and ensure it is named `index.html`.

Typical Import:
  >>> import flask_game_engine as fge

To run the Flask server, use:
  >>> fge.app.run()

Flask may appear not to load, however, its initialisation messages that are usually printed
to the console are now written to an `info.log` file. If this file doesn't exist, running the
application should create it in the same directory that the module is stored in.

You will find the website address written in this `info.log` file as well.

Public Functions:
 - home_page()
 - move()
 - send_game_state_to_user()
 - load_user_saved_game_state_bytes()
 - reset_board()
 - toggle_ai_opponent()

Private Helper Functions:
 - _any_legal_moves()
 - _save_game_state_to_file()
 - _load_game_state_from_file()
 - _load_config_data()
 - _determine_winner()
 - _check_for_empty_cells()
 - _check_for_other_players_colour()


### Brief Function Descriptions
#### 1. home_page():
Accessed by visiting `/`.

This function reads the `config.json` file, starts a new game and stores this new game in
the `game_state.json` file.


#### 2. move():
Accessed through `/move`.

This function deals with the logic behind verifying a move, switching players and
incorporating the AI opponent.

It takes 2 optional arguments in the URL - `x` and `y`, utilising the HTTP GET method.
Example URL: `/move?x=3&y=4`. Here, `x=3` and `y=4`.


#### 3. send_game_state_to_user():
Accessed through `/send_game_state_to_user` and utilises the HTTP POST method.

Receives the game log as plain text, updates the game state and sends the user a json file
of the current game state that their browser downloads automatically.


#### 4. load_user_saved_game_state_bytes():
Accessed through `/load_game_board` and utilises the HTTP POST method.

Allows the user to load a previously saved `game_state.json` file and continue their game
where they left off.


#### 5. reset_board():
Accessed through `/reset_board`.

Allows the user to start a new game.


#### 6. toggle_ai_opponent():
Accessed through `/toggle_ai_opponent` and utilises the HTTP POST method.

Facilitates the toggling of the AI opponent on or off.


#### 7. _any_legal_moves(colour: str, board: list[list[str]]):
Uses the current state of the board and the specified player colour to determine if this player
has at least one legal move available, if so True is returned, otherwise False is returned.


#### 8. _save_game_state_to_file(current_game_state: dict):
Saves the provided game state to the `game_state.json` file.


#### 9. _load_game_state_from_file():
Loads the game state from the `game_state.json` file and returns it as a python dictionary.


#### 10. _load_config_data():
Loads the config data from the `config.json` file and is used in `home_page()`.


#### 11. _determine_winner(board: list[list[str]]):
Given the current state of the board, determine which colour has won.

This is done by counting the number of each player's counter. The player
with the most counters wins.


#### 12. _check_for_empty_cells(board: list[list[str]]):
Searches the board for an empty cell, if at least one is found,
True is returned, otherwise False is returned.


#### 13. _check_for_other_players_colour(colour: str, board: list[list[str]]):
Given a player's colour, it searches the board for this colour. If at least one counter
of this colour is found, True is returned, otherwise False is returned.
"""

import os
import json
import logging
from time import sleep
from flask import Flask, render_template, request, Response
import components as comp
import ai_opponent as aio


# Create a Flask app with this file as the main entry point
app = Flask(__name__)

# Access the log and game_state file relative to the python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ERROR_LOG_PATH = os.path.join(BASE_DIR, "error.log")
INFO_LOG_PATH = os.path.join(BASE_DIR, "info.log")
GAME_STATE_PATH = os.path.join(BASE_DIR, "game_state.json")
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

# Set up the info logger
logging.basicConfig(filename=INFO_LOG_PATH, filemode="a", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
info_logger = logging.getLogger()

# Set up the error logger
logging.basicConfig(filename=ERROR_LOG_PATH, filemode="a", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")
error_logger = logging.getLogger()


def _any_legal_moves(colour: str, board: list[list[str]]) -> bool:
    """
    Given a player's colour, determine if they have at least one legal move available.
    """

    for row in range(len(board[0])):
        for column in range(len(board[0])):
            # If cell contains "None ", check if a legal cell
            if board[row][column] == "None ":
                is_legal_cell = comp.legal_move(colour, (column+1, row+1), board, False)

                # If cell is legal, return True
                if is_legal_cell['is_legal_move'] is True:
                    return True
    return False


def _save_game_state_to_file(current_game_state: dict) -> bool:
    """Takes a Python dictionary representing the current 
    games state and saves it to a JSON game state file."""

    with open(GAME_STATE_PATH, 'w', encoding='utf-8') as game_state_file:
        json.dump(current_game_state, game_state_file, indent=4)


def _load_game_state_from_file() -> dict:
    """Loads the game state from the JSON game state file."""

    with open(GAME_STATE_PATH, 'r', encoding='utf-8') as game_state_file:
        game_state = json.load(game_state_file)

    return game_state


def _load_config_data() -> dict:
    """Loads the config data to use in the game_state file."""

    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        config_data = json.load(config_file)

    return config_data


def _determine_winner(board: list[list[str]]) -> dict:
    """Counts the number of counters of each colour. 
    Then, calculates which colour is the winner, or if it is a draw."""

    # Initialise player score counters
    light_counter = 0
    dark_counter = 0

    # Calculate the number of counters for the other player
    for row in board:
        for cell in row:
            if cell == "Dark ":
                dark_counter += 1
            elif cell == "Light":
                light_counter += 1

    # Determine who is the winner
    if dark_counter > light_counter:
        winner = "Dark "
    elif dark_counter == light_counter:
        winner = "draw"
    else:
        winner = "Light"

    return {
        'finished': True,
        'scores': (light_counter, dark_counter),
        'winner': winner,
        'board': board
    }


def _check_for_empty_cells(board: list[list[str]]) -> bool:
    """Searches through the board and returns True if 
    the board contains at least one empty cell, otherwise it returns False."""

    for row in board:
        for cell in row:
            if cell == "None ":
                return True

    return False


def _check_for_other_players_colour(colour: str, board: list[list[str]]) -> bool:
    """Searches the board for a counter of the specified colour.\n
    Returns True if at least one counter of the specified colour
    is present, otheriwse it returns False."""

    for row in board:
        for cell in row:
            if cell == colour:
                return True
    return False


@app.route('/')
def home_page():
    """Executed every time the webpage is visited.\n
    Resets some variables and saves them to the game state file."""

    # Load the config data
    config_data = _load_config_data()

    # Reset the game state variables
    board = comp.initialise_board()
    _save_game_state_to_file({
        'board': board,
        'game_over': config_data['initial_game_over_status'],
        'move_counter': config_data['default_move_counter'],
        'current_player': config_data['start_player'],
        'game_log': config_data['game_log'],
        'ai_opponent_toggle': config_data['ai_opponent_toggle'],
        'ai_move': config_data['ai_move']
    })

    return render_template("index.html", game_board=board)


@app.route('/move', methods=['GET'])
def move() -> dict:
    """
    Deals with verifying and making a move.
    """

    try:
        # Load the game state
        game_state = _load_game_state_from_file()

        # Extract the x and y coordinates for the move
        x_coord = int(request.args['x'])
        y_coord = int(request.args['y'])

        # Ensure the coordinates are within the boundaries of the board
        if (x_coord < 1 or x_coord > len(game_state['board'])
            or y_coord < 1 or y_coord > len(game_state['board'])):

            error_logger.error("Coordinates were outside the boundaries of the board.")
            return {
                'status': 'fail',
                'error_message': "Coordinates were outside the boundaries of the board."
            }

        # First check if there are any empty cells, the game is over or there are any moves left
        if (_check_for_empty_cells(game_state['board']) is False
                or game_state['game_over'] is True
                or game_state['move_counter'] <= 0):

            # Set game_over to true
            game_state['game_over'] = True
            _save_game_state_to_file(game_state)
            # Calculate the winner and retrun the results
            return _determine_winner(game_state['board'])

        # === AI Opponent Section ===
        # Check if the AI opponent is enabled and it is the AI's turn
        if game_state['ai_opponent_toggle'] is True and game_state['current_player'] == "Light":
            # This delay is used to allow time for the human player
            # to understand the board's new state once they have placed their own counter
            sleep(0.8)

            # Get the AI to make a move
            ai_move = aio.calculate_move(game_state['board'])

            # Check that the AI could make a move
            if ai_move == (-1,-1):
                # AI decided that it couldn't make a move
                # Switch players
                game_state['current_player'] = "Dark "

                # Save the new game state
                _save_game_state_to_file(game_state)
                error_logger.error(game_state['current_player'])

                return {
                    'status': 'fail',
                    'next_player': game_state['current_player']
                }

            # Otherwise, extract the ai_move coordinates and assign them to the x and y coords
            x_coord = ai_move[0]
            y_coord = ai_move[1]

            # Update the game state
            game_state['ai_move'] = ai_move

        # Make the move
        move_results = comp.legal_move(game_state['current_player'],
                                        (x_coord, y_coord),
                                        game_state['board'], True)

        # Check if the chosen move is legal
        if move_results['is_legal_move'] is False:
            return {
                'status': 'fail',
                'error_message': f"Illegal move at ({x_coord},{y_coord})."
            }

        # Update the board
        game_state['board'] = move_results['board']
        # Decrement the move counter
        game_state['move_counter'] -= 1

        # Check if there are any free cells on the board after this move was made
        # If no free cells are present, game is over - since no one will be able to place a counter
        if _check_for_empty_cells(game_state['board']) is False:
            game_state['game_over'] = True
            _save_game_state_to_file(game_state)
            return _determine_winner(game_state['board'])

        # Determine the other player
        if game_state['current_player'] == "Dark ":
            other_player = "Light"
        else:
            other_player = "Dark "

        # Now check if the other player can make a move
        if _any_legal_moves(other_player, game_state['board']) is False:
            # Check if the current player can make a move
            if _any_legal_moves(game_state['current_player'], game_state['board']) is False:
                # Therefore, game is over
                game_state['game_over'] = True
                # Calculate and return the winner
                return _determine_winner(game_state['board'])

            # Otherwise, other player cannot make a move but the current player can
            # However, if no counter of the other player's colour is present on the board,
            # the game is still over
            if _check_for_other_players_colour(other_player, game_state['board']) is False:
                _save_game_state_to_file(game_state)
                return _determine_winner(game_state['board'])

            # If counters are present of the other player's colour, then the game can continue
            # Save the new game state to file
            if _save_game_state_to_file(game_state) is False:
                logging.error("Unable to save game state when other " \
                "player doesn't have an legal moves.")

            # Return the status that the other player cannot make any legal moves,
            # but the current one can, effectively skipping the other player's turn
            return {
                'status': 'success',
                'board': game_state['board'],
                'current_player': game_state['current_player'],
                'other_player': other_player,
                'ai_coordinate': game_state['ai_move'],
                'legal_moves_available_for_other_player': False
            }

        # Finally, if there are free cells left and the other player can make a move
        # Switch players and continue as normal
        if game_state['current_player'] == "Dark ":
            game_state['current_player'] = "Light"
        else:
            game_state['current_player'] = "Dark "

        # Save the new state of the game
        if _save_game_state_to_file(game_state) is False:
            error_logger.error("Unable to save game state when both " \
            "players can make a legal move.")

        # Return the new state of the board and the next player
        return {
            'status': 'success',
            'board': game_state['board'],
            'next_player': game_state['current_player'],
            'ai_coordinate': game_state['ai_move'],
            'legal_moves_available_for_other_player': True
        }
    except FileExistsError as e:
        error_logger.error(e)
        return {
            'status': 'fail',
            'error_message': e
        }
    except FileNotFoundError as e:
        error_logger.error(e)
        return {
            'status': 'fail',
            'error_message': e
        }


@app.route('/send_game_state_to_user', methods=['POST'])
def send_game_state_to_user() -> Response:
    """Allows the user to download the current game state as a JSON file."""

    # First load the current game state
    game_state = _load_game_state_from_file()

    # Extract the game log text
    game_state['game_log'] = request.get_data(as_text=True)

    # Convert the python dictionary to a json string
    # .encode("utf-8") - converts the python string to bytes so the browser can download the file
    json_bytes = json.dumps(game_state, indent=4).encode("utf-8")

    # Create and return a custom Flask Response object
    return Response(
        # The file content the user will download
        json_bytes,
        # Tells the browser what file type it is - in this case, the file type is json
        mimetype="application/json",
        # This is the part which forces the browser to download the file instead of displaying it
        #   attachment - triggers the file download
        #   filename=data.json - tells the browser which file name to use
        headers={"Content-Disposition": "attachment; filename=reversi_game_board_save.json"}
    )


@app.route('/load_game_board', methods=['POST'])
def load_user_saved_game_state_bytes() -> dict:
    """Allows the user to provide a previously saved game state JSON file."""

    # Load the current game state
    game_state = _load_game_state_from_file()

    # Extract the file from the request
    user_saved_game_state_bytes = request.files.get('file')

    # If file is empty, return error message
    if not user_saved_game_state_bytes:
        return {
            'status': "fail",
            'error_message': "No file received!"
        }

    # Read the contents of the file
    file_bytes = user_saved_game_state_bytes.read()

    # Convert bytes to string to Python object
    try:
        user_saved_game_state = json.loads(file_bytes.decode("utf-8"))
    except json.JSONDecodeError:
        return {
            'status': "fail",
            'error_message': "Invalid JSON file!"
        }

    # Extract the required information from the file
    game_state['board'] = user_saved_game_state['board']
    game_state['game_over'] = user_saved_game_state['game_over']
    game_state['move_counter'] = user_saved_game_state['move_counter']
    game_state['current_player'] = user_saved_game_state['current_player']
    game_state['game_log'] = user_saved_game_state['game_log']
    game_state['ai_opponent_toggle'] = user_saved_game_state['ai_opponent_toggle']

    # Save the new game state
    if _save_game_state_to_file(game_state) is False:
        error_logger.error("Unable to save user saved game state.")

    # Return success status and new board state
    return {
        'status': 'success',
        'board': game_state['board'],
        'current_player': game_state['current_player'],
        'game_over': game_state['game_over'],
        'game_log': game_state['game_log'],
        'ai_opponent_toggle': game_state['ai_opponent_toggle']
    }


@app.route('/reset_board')
def reset_board() -> dict:
    """Resets the board and other game state variables."""

    # Load the current game_state
    game_state = _load_game_state_from_file()

    # First initialise a new board
    game_state['board'] = comp.initialise_board()
    # Reset the move counter
    game_state['move_counter'] = 60
    # Change the current player back to Dark
    game_state['current_player'] = "Dark "
    # Set game over to false
    game_state['game_over'] = False

    # Save the new game state to file
    if _save_game_state_to_file(game_state) is False:
        error_logger.error("Unable to save game state once reset board.")

    # Return success status and the new board
    return {
        'status': 'success',
        'board': game_state['board'],
        'current_player': game_state['current_player']
    }


@app.route("/toggle_ai_opponent", methods=['POST'])
def toggle_ai_opponent() -> dict:
    """Allows the user to enable and disable the AI opponent."""

    try:
        # Load the current game state
        game_state = _load_game_state_from_file()

        # Retrieve the new value of the toggle
        user_checkbox_checked_state = request.get_data(as_text=True)

        # Change the global value accordingly
        if user_checkbox_checked_state == "true":
            game_state['ai_opponent_toggle'] = True
        else:
            game_state['ai_opponent_toggle'] = False

        # Save the new game state to file
        if _save_game_state_to_file(game_state) is False:
            error_logger.error("Unable to save game state when toggling the AI opponent.")

        # Return status
        return {'status': 'success'}
    except FileNotFoundError as e:
        logging.exception(e)
        return {
            'status': 'fail',
            'error_message': e
        }


# Only run the app if the current file is being run directly
if __name__ == "__main__":
    # Start the local web server
    # When debug=True, any change to the python files
    # will cause an automatic server reboot
    app.run()
