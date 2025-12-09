"""..."""

import json
from time import sleep
from flask import Flask, render_template, request, Response
import numpy as np
import components as comp
import ai_opponent as aio

# Create a Flask app with this file as the main entry point
app = Flask(__name__)


def any_legal_moves(colour: str, board: list[list[str]]) -> bool:
    """Given a player's colour, determine if any legal moves remain."""
    # Initialise legalMove
    legal_move = False
    size = len(board[0])

    for row in range(size):
        for column in range(size):
            # If cell contains "None ", check if a legal cell
            if board[row, column] == "None ":
                is_legal_cell = comp.legal_move(colour, (column+1, row+1), board, False)

                # If cell is legal, set legalMove to True
                if is_legal_cell:
                    legal_move = True

    # Return whether the player can make a legal move
    return legal_move


def save_game_state_to_file(current_game_state: dict) -> bool:
    """Takes a Python dictionary representing the current 
    games state and saves it to a JSON game state file."""

    with open('./game_state.json', 'w', encoding='utf-8') as game_state_file:
        json.dump(current_game_state, game_state_file)


def load_game_state_from_file() -> dict:
    """Loads the game state from the JSON file."""

    with open('./game_state.json', 'r', encoding='utf-8') as game_state_file:
        game_state = json.load(game_state_file)

    return game_state


@app.route('/')
def home_page():
    """Executed every time the webpage is visited.\n
    Resets some variables and saves them to the game state file."""

    # Reset the game state variables
    board = comp.initialise_board().tolist()
    save_game_state_to_file({
        'board': board,
        'game_over': False,
        'move_counter': 60,
        'current_player': "Dark ",
        'game_log': request.get_data(as_text=True),
        'ai_opponent_toggle': False
    })

    return render_template("index.html", game_board=board)


def determine_winner(board: list[list[str]]) -> dict:
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
        'board': board.tolist()
    }


def check_for_empty_cells(board: list[list[str]]) -> bool:
    """Searches through the board and returns True if 
    the board contains at least one empty cell, otherwise it returns False."""

    for row in board:
        for cell in row:
            if cell == "None ":
                return True

    return False


def check_for_other_players_colour(colour: str, board: list[list[str]]) -> bool:
    """Searches the board for a counter of the specified colour.\n
    Returns True if at least one counter of the specified colour
    is present, otheriwse it returns False."""

    for row in board:
        for cell in row:
            if cell == colour:
                return True
    return False


@app.route('/move', methods=['GET'])
def move() -> dict:
    """Deals with verifying and making a move."""

    # Load the game state
    game_state = load_game_state_from_file()

    # Ensure this function can deal with the GET method
    if request.method == 'GET':
        x_coord = int(request.args['x'])
        y_coord = int(request.args['y'])
    else:
        return {'status': 'error'}

    # First check if there are any empty cells, the game is over or there are any moves left
    if (check_for_empty_cells(game_state['board']) is False
            or game_state['game_over'] is True
            or game_state['move_counter'] <= 0):

        # Board is full, so set game_over to true
        game_state['game_over'] = True
        # Calculate the winner and retrun the results
        return determine_winner(game_state['board'])

    # Check if the AI opponent is enabled and it is the AI's turn
    if game_state['ai_opponent_toggle'] is True and game_state['current_player'] == "Light":
        # This delay is used to allow time for the human player
        # to read the board's state once they have placed their counter
        sleep(0.8)

        # Get the AI to make a move
        ai_move = aio.makeMove(game_state['board'])

        # Check that the AI could make a move
        if ai_move == (-1,-1):
            # AI decided that it couldn't make a move
            # Switch players
            game_state['current_player'] = "Dark "
            return {
                'status': 'fail',
                'next_player': game_state['current_player']
            }

        # Otherwise, extract the ai_move coordinates and assign them to the x and y coords
        x_coord = ai_move[0]
        y_coord = ai_move[1]

    # Make the move
    is_legal_move = comp.legal_move(game_state['current_player'],
                                    (x_coord, y_coord),
                                    game_state['board'], True)

    # Check if the chosen move is legal
    if is_legal_move is False:
        return {'status': 'fail'}

    # Check if there are any free cells on the board after this move was made
    # If no free cells are present, game is over - since no one will be able to place a counter
    if check_for_empty_cells(game_state['board']) is False:
        game_state['game_over'] = True
        return determine_winner(game_state['board'])

    # Determine the other player
    if game_state['current_player'] == "Dark ":
        other_player = "Light"
    else:
        other_player = "Dark "

    # Now check if the other player can make a move
    if any_legal_moves(other_player, game_state['board']) is False:
        # Check if the current player can make a move
        if any_legal_moves(game_state['current_player'], game_state['board']) is False:
            # Therefore, game is over
            game_state['game_over'] = True
            # Calculate and return the winner
            return determine_winner(game_state['board'])

        # Otherwise, other player cannot make a move but the current player can
        # However, if no counter of the other player's colour is present on the board,
        # the game is still over
        if check_for_other_players_colour(other_player, game_state['board']) is False:
            return determine_winner(game_state['board'])

        # If counters are present of the other player's colour, then the game can continue
        # Save the new game state to file
        if save_game_state_to_file(game_state) is False:
            # TODO: Log error to log file
            print(" === Error: Unable to save game state when " \
                "other player doesn't have any legal moves")

        # Return the status that the other player cannot make any legal moves,
        # but the current one can, effectively skipping the other player's turn
        return {
            'status': 'success',
            'board': game_state['board'].tolist(),
            'current_player': game_state['current_player'],
            'other_player': other_player,
            'ai_coordinate': ai_move,
            'legal_moves_available_for_other_player': False
        }

    # Finally, if there are free cells left and the other player can make a move
    # Switch players and continue as normal
    if game_state['current_player'] == "Dark ":
        game_state['current_player'] = "Light"
    else:
        game_state['current_player'] = "Dark "

    # Save the new state of the game
    if save_game_state_to_file(game_state) is False:
        # TODO: Log error to log file
        print(" === Error: Unable to save game state when both players can make a legal move")

    # Return the new state of the board and the next player
    return {
        'status': 'success',
        'board': game_state['board'].tolist(),
        'next_player': game_state['current_player'],
        'ai_coordinate': ai_move,
        'legal_moves_available_for_other_player': True
    }


@app.route('/send_game_state_to_user', methods=['POST'])
def send_game_state_to_user() -> Response:
    """Allows the user to download the current game state as a JSON file."""

    # First load the current game state
    game_state = load_game_state_from_file()

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


# Function that loads a previous reversi game
@app.route('/load_game_board', methods=['POST'])
def load_user_saved_game_state_bytes() -> dict:
    """Allows the user to provide a previously saved game state JSON file."""

    # Load the current game state
    game_state = load_game_state_from_file()

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
    game_state['board'] = np.array(user_saved_game_state['board'])
    game_state['game_over'] = user_saved_game_state['game_over']
    game_state['move_counter'] = user_saved_game_state['move_counter']
    game_state['current_player'] = user_saved_game_state['current_player']
    game_state['game_log'] = user_saved_game_state['game_log']
    game_state['ai_opponent_toggle'] = user_saved_game_state['ai_opponent_toggle']

    # Save the new game state
    if save_game_state_to_file(game_state) is False:
        # TODO: Log error to log file
        print(" === Error: Unable to save user saved game state")

    # Return success status and new board state
    return {
        'status': 'success',
        'board': game_state['board'].tolist(),
        'current_player': game_state['current_player'],
        'game_over': game_state['game_over'],
        'game_log': game_state['game_log'],
        'ai_opponent_toggle': game_state['ai_opponent_toggle']
    }


# Function that resets the board, ready for a new game
@app.route('/reset_board')
def reset_board() -> dict:
    """Resets the board and other game state variables."""

    # Load the current game_state
    game_state = load_game_state_from_file()

    # First initialise a new board
    game_state['board'] = comp.initialise_board()

    # Reset the move counter
    game_state['move_counter'] = 60

    # Change the current player back to Dark
    game_state['current_player'] = "Dark "

    # Set game over to false
    game_state['game_over'] = False

    # Save the new game state to file
    if save_game_state_to_file(game_state) is False:
        # TODO: Log error to log file
        print(" === Error: Unable to save game state once reset board.")

    # Return success status and the new board
    return {
        'status': 'success',
        'board': game_state['board'].tolist(),
        'current_player': game_state['current_player']
    }


@app.route("/toggle_ai_opponent", methods=['POST'])
def toggle_ai_opponent() -> dict:
    """Allows the user to enable and disable the AI opponent."""

    # Load the current game state
    game_state = load_game_state_from_file()

    try:
        # Retrieve the new value of the toggle
        user_checkbox_checked_state = request.get_data(as_text=True)

        # Change the global value accordingly
        if user_checkbox_checked_state == "true":
            game_state['ai_opponent_toggle'] = True
        else:
            game_state['ai_opponent_toggle'] = False

        # Save the new game state to file
        if save_game_state_to_file(game_state) is False:
            # TODO: Log error to log file
            print(" === Error: Unable to save game state when toggling the AI opponent.")

        # Return status
        return {'status': 'success'}
    except Exception as e:
        return {
            'status': 'fail',
            'error_message': e
        }


# Only run the app if the current file is being run directly
if __name__ == "__main__":
    # Start the local web server
    # When in debug mode, any change to the python files
    # will cause an automatic server reboot
    app.run()
