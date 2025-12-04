from flask import Flask, render_template, request
import components as comp

# Create a Flask app with this file as the main entry point
app = Flask(__name__)


# Function determines if any legal moves remain for a given player
def any_legal_moves(colour, board):
    # Initialise legalMove
    legalMove = False

    for row in range(len(board[0])):
        for column in range(len(board[0])):
            # If cell contains "None ", check if a legal
            if (board[row, column] == "None "):
                isLegalCell = comp.legal_move(colour, (column, row), board, False)
            
                # If cell is legal, set legalMove to True
                if (isLegalCell): legalMove = True
    
    # Return whether the player can make a legal move
    return legalMove


# Initialise the board
board = comp.initialise_board()

# Initialise global game over tracker
gameOver = False

# Initialise the move counter
moveCounter = 60

# Set the starting player
currentPlayer = "Dark "


# Decorator that tells Flask to run this func when '/' is visited
@app.route('/')
def home_page():
	return render_template("index.html", game_board=board.tolist())


# Function that handles when a player makes a move
@app.route('/move', methods=['GET'])
def move():
    # Ensure python modifies the global version of these variables
    global board
    global currentPlayer
    global moveCounter
    global gameOver

    # If game is over, exit function
    if (gameOver): return {'status': 'game_over'}

    # Ensure this function can deal with the GET method
    if request.method == 'GET':
        xCoord = int(request.args['x'])
        yCoord = int(request.args['y'])
    else: return {'status': 'error'}
    
    # Check if there are any legal moves available for the current player
    if (not any_legal_moves(currentPlayer, board)):
        # Determine the other player
        if (currentPlayer == "Dark "): otherPlayer = "Light"
        else: otherPlayer = "Dark "

        # Check whether either player can make a move
        if (not any_legal_moves(otherPlayer, board)):
            # Therefore, game is over
            # Initialise player score counters
            lightCounter = 0
            darkCounter = 0

            # Calculate the number of counters for each player
            for row in board:
                for cell in row:
                    if (cell == "Dark "): darkCounter += 1
                    elif (cell == "Light"): lightCounter += 1
            
            # Determine who is the winner
            if (darkCounter > lightCounter): winner = "Dark"
            else: winner = "Light"
            
            gameOver = True
            # Return finished=True and player scores
            return {
                 'finished': True,
                 'scores': (lightCounter, darkCounter),
                 'winner': winner,
                 'board': board.tolist()
            }

        previousPlayer = currentPlayer
        
        # Switch to other player
        if (currentPlayer == "Dark "): currentPlayer = "Light"
        else: currentPlayer = "Dark "

        # Return status=no_legal_moves
        return {
            'status': 'no_legal_moves',
            'player': previousPlayer
        }

    # Check whether the move is legal
    isLegalMove = comp.legal_move(currentPlayer, (xCoord, yCoord), board, True)
    if (not isLegalMove): 
        # Inform the player that this is not a legal move
        return {
            'status': 'fail',
            'message': 'illegal move'
        }
    
    otherPlayerCounter = 0
    # Determine the other player
    if (currentPlayer == "Dark "): otherPlayer = "Light"
    else: otherPlayer = "Dark "
    # Initialise player score counters
    lightCounter = 0
    darkCounter = 0
    # Calculate the number of counters for the other player
    for row in board:
        for cell in row:
            if (cell == otherPlayer): otherPlayerCounter += 1
            if (cell == "Dark "): darkCounter += 1
            if (cell == "Light"): lightCounter += 1
    
    # Determine who is the winner
    if (darkCounter > lightCounter): winner = "Dark"
    else: winner = "Light"
    
    # If no of the other player's counters are present, game is over
    if (otherPlayerCounter == 0):
        gameOver = True
        return {
            'finished': True,
            'scores': (lightCounter, darkCounter),
            'winner': winner,
            'board': board.tolist()
        }
    
    # Switch to other player
    if (currentPlayer == "Dark "): currentPlayer = "Light"
    else: currentPlayer = "Dark "
    
    # Return the success status and the new state of the board
    return {
        'status': 'success',
        'board': board.tolist(),
        'player': currentPlayer
    }


# Only run the app if the current file is being run directly
if __name__ == "__main__":
    app.run() # Start the local web server

