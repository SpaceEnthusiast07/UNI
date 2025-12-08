from flask import Flask, render_template, request, Response, jsonify
import components as comp
import json, time
import numpy as np
import ai_opponent as aio

# Create a Flask app with this file as the main entry point
app = Flask(__name__)


# Function determines if any legal moves remain for a given player
def any_legal_moves(colour, board):
    # Initialise legalMove
    legalMove = False
    size = len(board[0])

    for row in range(size):
        for column in range(size):
            # If cell contains "None ", check if a legal cell
            if (board[row, column] == "None "):
                isLegalCell = comp.legal_move(colour, (column+1, row+1), board, False)
            
                # If cell is legal, set legalMove to True
                if (isLegalCell): legalMove = True
    
    # Return whether the player can make a legal move
    return legalMove


# Initialise the board
board = comp.initialise_board()
# Initialise global game over tracker
gameOver = False
# Initialise the move counter
moveCounter = 64
# Set the starting player
currentPlayer = "Dark "
# Initialise the ai opponent toggle to false
aiOpponentToggle = False
# Initialise ai_move dummy value
ai_move = (0,0)


# Decorator that tells Flask to run this func when '/' is visited
@app.route('/')
def home_page():
    global board
    global gameOver
    global moveCounter
    global currentPlayer
    global aiOpponentToggle

    # Re-initialise the board, gameOver, moveCounter and currentPlayer
    board = comp.initialise_board()
    gameOver = False
    moveCounter = 64
    currentPlayer = "Dark "
    aiOpponentToggle = False

    return render_template("index.html", game_board=board.tolist())


def determineWinner():
    # Initialise player score counters
    lightCounter = 0
    darkCounter = 0
    # Calculate the number of counters for the other player
    for row in board:
        for cell in row:
            if (cell == "Dark "): darkCounter += 1
            elif (cell == "Light"): lightCounter += 1
    
    # Determine who is the winner
    if (darkCounter > lightCounter): winner = "Dark "
    elif (darkCounter == lightCounter): winner = "draw"
    else: winner = "Light"
    
    return {
        'finished': True,
        'scores': (lightCounter, darkCounter),
        'winner': winner,
        'board': board.tolist()
    }


def checkForEmptyCells():
    for row in board:
        for cell in row:
            if (cell == "None "): return True
    return False


def checkForOtherPlayersColour(colour):
    for row in board:
        for cell in row:
            if (cell == colour): True
    return False


# Function that handles when a player makes a move
@app.route('/move', methods=['GET'])
def move():
    # Ensure python modifies the global version of these variables
    global board
    global currentPlayer
    global moveCounter
    global gameOver
    global ai_move

    # Ensure this function can deal with the GET method
    if request.method == 'GET':
        xCoord = int(request.args['x'])
        yCoord = int(request.args['y'])
    else: return {'status': 'error'}
    
    # First check if there are any empty cells, the game is over or there are any moves left
    if ((not checkForEmptyCells()) or (gameOver == True) or (moveCounter <= 0)):
        # Board is full, so set gameOver to true
        gameOver = True
        # Calculate the winner and retrun the results
        return determineWinner()
    
    # Check if the AI opponent is enabled and it is the AI's turn
    if ((aiOpponentToggle == True) and (currentPlayer == "Light")):
        # This delay is used to allow time for the human player to read the board's state once they have placed their counter
        time.sleep(0.8)
        # Get the AI to make a move
        ai_move = aio.makeMove(board)

        # Check that the AI could make a move
        if (ai_move == (-1,-1)):
            # AI decided that it couldn't make a move
            # Switch players
            currentPlayer = "Dark "
            return {
                'status': 'fail',
                'next_player': currentPlayer
            }
        
        # Otherwise, extract the ai_move coordinates and assign them to the x and y coords
        xCoord = ai_move[0]
        yCoord = ai_move[1]
    
    # Make the move
    isLegalMove = comp.legal_move(currentPlayer, (xCoord, yCoord), board, True)
    # Check if the chosen move is legal
    if (isLegalMove == False): 
        return {
            'status': 'fail'
        }
    
    # Check if there are any free cells on the board after this move was made
    # If no free cells are present, game is over - since no one will be able to place a counter
    if (checkForEmptyCells() == False):
        gameOver = True
        return determineWinner()
    
    # Determine the other player
    if (currentPlayer == "Dark "): otherPlayer = "Light"
    else: otherPlayer = "Dark "
    
    # Now check if the other player can make a move
    if (any_legal_moves(otherPlayer, board) == False):
        # Check if the current player can make a move
        if (any_legal_moves(currentPlayer, board) == False):
            # Therefore, game is over
            gameOver = True
            # Calculate and return the winner
            return determineWinner()
        
        # Otherwise, other player cannot make a move but the current player can
        # However, if no counter of the other player's colour is present on the board, the game is still over
        if (checkForOtherPlayersColour(otherPlayer) == False): return determineWinner()

        # If counters are present of the other player's colour, then the game can continue
        # Return the status that the other player cannot make any legal moves, but the current one can
        # effectively skipping the other player's turn
        return {
            'status': 'success',
            'board': board.tolist(),
            'current_player': currentPlayer,
            'other_player': otherPlayer,
            'ai_coordinate': ai_move,
            'legal_moves_available_for_other_player': False
        }
    
    # Finally, if there are free cells left and the other player can make a move
    # Switch players and continue as normal
    if (currentPlayer == "Dark "): currentPlayer = "Light"
    else: currentPlayer = "Dark "

    # Return the new state of the board and the next player
    return {
        'status': 'success',
        'board': board.tolist(),
        'next_player': currentPlayer,
        'ai_coordinate': ai_move,
        'legal_moves_available_for_other_player': True
    }



# Function that allows the user to save the state of the game to their computer
@app.route('/same_game_board', methods=['POST'])
def saveGameBoard():
    # Create the json object to store in the json file
    gameBoardFile = {
        'board': board.tolist(),
        'game_over': gameOver,
        'move_counter': moveCounter,
        'current_player': currentPlayer,
        'game_log': request.get_data(as_text=True),
        'ai_opponent_toggle': "on" if aiOpponentToggle == True else "off"
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
    global moveCounter
    global currentPlayer
    global gameOver
    global aiOpponentToggle

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
    gameOver = gameBoardFile['game_over']
    moveCounter = gameBoardFile['move_counter']
    currentPlayer = gameBoardFile['current_player']
    gameLog = gameBoardFile['game_log']
    aiOpponentToggle = True if gameBoardFile['ai_opponent_toggle'] == "on" else False

    # Return success status and new board state
    return {
        'status': 'success',
        'board': board.tolist(),
        'current_player': currentPlayer,
        'game_over': gameOver,
        'game_log': gameLog,
        'ai_opponent_toggle': aiOpponentToggle
    }


# Function that resets the board, ready for a new game
@app.route('/reset_board')
def resetBoard():
    # Ensure python accesses the global variables
    global board
    global moveCounter
    global currentPlayer
    global gameOver

    # First initialise a new board
    board = comp.initialise_board()

    # Reset the move counter
    moveCounter = 64

    # Change the current player back to Dark
    currentPlayer = "Dark "

    # Set game over to false
    gameOver = False

    # Return success status and the new board
    return {
        'status': 'success',
        'board': board.tolist(),
        'current_player': currentPlayer
    }



@app.route("/toggle_ai_opponent", methods=['POST'])
def toggleAIOpponent():
    # Ensure this function accesses the global variable
    global aiOpponentToggle

    try:
        # Retrieve the new value of the toggle
        toggleValue = request.get_data(as_text=True)

        # Change the global value accordingly
        if (toggleValue == "true"): aiOpponentToggle = True
        else: aiOpponentToggle = False

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

