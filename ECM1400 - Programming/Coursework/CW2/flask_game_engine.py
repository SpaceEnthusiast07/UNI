"""..."""

import json
from time import sleep
from flask import Flask, render_template, request, Response
import components as comp
import numpy as np
import ai_opponent as aio

# Create a Flask app with this file as the main entry point
app = Flask(__name__)


def any_legal_moves(colour: str) -> bool:
    """Given a player's colour, determine if any legal moves remain"""
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


def save_game_state_to_file(current_game_state: {list[list[str]],bool,int,str,str,bool}) -> bool:
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


def determine_winner(board: list[list[str]]):
    """Counts the number of counters of each colour. 
    Calculates which colour is the winner, or if it is a draw."""

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


def check_for_empty_cells(board: list[list[str]]):
    """Searches through the board and returns True if 
    the board contains at least one empty cell, otherwise it returns False."""

    for row in board:
        for cell in row:
            if cell == "None ":
                return True

    return False


def checkForOtherPlayersColour(colour):
    for row in board:
        for cell in row:
            if (cell == colour): True
    return False


# Function that handles when a player makes a move
@app.route('/move', methods=['GET'])
def move():
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
    if ((not check_for_empty_cells()) or (game_over == True) or (move_counter <= 0)):
        # Board is full, so set game_over to true
        game_over = True
        # Calculate the winner and retrun the results
        return determine_winner()
    
    # Check if the AI opponent is enabled and it is the AI's turn
    if ((ai_opponent_toggle == True) and (current_player == "Light")):
        # This delay is used to allow time for the human player to read the board's state once they have placed their counter
        sleep(0.8)
        # Get the AI to make a move
        ai_move = aio.makeMove(board)

        # Check that the AI could make a move
        if (ai_move == (-1,-1)):
            # AI decided that it couldn't make a move
            # Switch players
            current_player = "Dark "
            return {
                'status': 'fail',
                'next_player': current_player
            }
        
        # Otherwise, extract the ai_move coordinates and assign them to the x and y coords
        x_coord = ai_move[0]
        y_coord = ai_move[1]
    
    # Make the move
    isLegalMove = comp.legal_move(current_player, (x_coord, y_coord), board, True)
    # Check if the chosen move is legal
    if (isLegalMove == False): 
        return {
            'status': 'fail'
        }
    
    # Check if there are any free cells on the board after this move was made
    # If no free cells are present, game is over - since no one will be able to place a counter
    if (check_for_empty_cells() == False):
        game_over = True
        return determine_winner()
    
    # Determine the other player
    if (current_player == "Dark "): otherPlayer = "Light"
    else: otherPlayer = "Dark "
    
    # Now check if the other player can make a move
    if (any_legal_moves(otherPlayer, board) == False):
        # Check if the current player can make a move
        if (any_legal_moves(current_player, board) == False):
            # Therefore, game is over
            game_over = True
            # Calculate and return the winner
            return determine_winner()
        
        # Otherwise, other player cannot make a move but the current player can
        # However, if no counter of the other player's colour is present on the board, the game is still over
        if (checkForOtherPlayersColour(otherPlayer) == False): return determine_winner()

        # If counters are present of the other player's colour, then the game can continue
        # Return the status that the other player cannot make any legal moves, but the current one can
        # effectively skipping the other player's turn
        return {
            'status': 'success',
            'board': board.tolist(),
            'current_player': current_player,
            'other_player': otherPlayer,
            'ai_coordinate': ai_move,
            'legal_moves_available_for_other_player': False
        }
    
    # Finally, if there are free cells left and the other player can make a move
    # Switch players and continue as normal
    if (current_player == "Dark "): current_player = "Light"
    else: current_player = "Dark "

    # Return the new state of the board and the next player
    return {
        'status': 'success',
        'board': board.tolist(),
        'next_player': current_player,
        'ai_coordinate': ai_move,
        'legal_moves_available_for_other_player': True
    }


# Function that allows the user to save the state of the game to their computer
@app.route('/same_game_board', methods=['POST'])
def saveGameBoard():
    # Create the json object to store in the json file
    gameBoardFile = {
        'board': board.tolist(),
        'game_over': game_over,
        'move_counter': move_counter,
        'current_player': current_player,
        'game_log': request.get_data(as_text=True),
        'ai_opponent_toggle': "on" if ai_opponent_toggle == True else "off"
    }

    # Convert the python dictionary to a json string
    # .encode("utf-8") - converts the python string to bytes so the browser can download the file
    json_bytes = json.dumps(gameBoardFile, indent=4).encode("utf-8")

    # Create and return a custom Flask Response object
    return Response(
        json_bytes, # The file content the user will download
        mimetype="application/json", # Tells the browser what file type it is - in this case, the file type is json
        # This is the part which forces the browser to download the file instead of displaying it
        # attachment - triggers the file download
        # filename=data.json - tells the browser which file name to use
        headers={"Content-Disposition": "attachment; filename=reversi_game_board_save.json"}
    )


# Function that loads a previous reversi game
@app.route('/load_game_board', methods=['POST'])
def loadGameBoard():
    # Ensure python accesses the global variables
    global board
    global move_counter
    global current_player
    global game_over
    global ai_opponent_toggle

    # Extract the file from the request
    sentFile = request.files.get('file')

    # If file is empty, return error message
    if (not sentFile): return {'status': "fail", 'error_message': "No file received!"}

    # Read the contents of the file
    file_bytes = sentFile.read()

    # Convert bytes to string to Python object
    try:
        gameBoardFile = json.loads(file_bytes.decode("utf-8"))
    except json.JSONDecodeError:
        return {'status': "fail", 'error_message': "Invalid JSON file!"}
    
    # Extract the required information from the file
    board = np.array(gameBoardFile['board'])
    game_over = gameBoardFile['game_over']
    move_counter = gameBoardFile['move_counter']
    current_player = gameBoardFile['current_player']
    gameLog = gameBoardFile['game_log']
    ai_opponent_toggle = True if gameBoardFile['ai_opponent_toggle'] == "on" else False

    # Return success status and new board state
    return {
        'status': 'success',
        'board': board.tolist(),
        'current_player': current_player,
        'game_over': game_over,
        'game_log': gameLog,
        'ai_opponent_toggle': ai_opponent_toggle
    }


# Function that resets the board, ready for a new game
@app.route('/reset_board')
def resetBoard():
    # Ensure python accesses the global variables
    global board
    global move_counter
    global current_player
    global game_over

    # First initialise a new board
    board = comp.initialise_board()

    # Reset the move counter
    move_counter = 64

    # Change the current player back to Dark
    current_player = "Dark "

    # Set game over to false
    game_over = False

    # Return success status and the new board
    return {
        'status': 'success',
        'board': board.tolist(),
        'current_player': current_player
    }


@app.route("/toggle_ai_opponent", methods=['POST'])
def toggleAIOpponent():
    # Ensure this function accesses the global variable
    global ai_opponent_toggle

    try:
        # Retrieve the new value of the toggle
        toggleValue = request.get_data(as_text=True)

        # Change the global value accordingly
        if (toggleValue == "true"): ai_opponent_toggle = True
        else: ai_opponent_toggle = False

        # Return status
        return {'status': 'success'}
    except:
        return {'status': 'fail'}


# Only run the app if the current file is being run directly
if __name__ == "__main__":
    # Start the local web server
    # When in debug mode, any change to the python files 
    # will cause an automatic server reboot
    app.run()
