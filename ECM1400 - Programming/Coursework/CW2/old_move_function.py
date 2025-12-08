# Function that handles when a player makes a move
@app.route('/move', methods=['GET'])
def move():
    # Ensure python modifies the global version of these variables
    global board
    global currentPlayer
    global moveCounter
    global gameOver

    # Ensure this function can deal with the GET method
    if request.method == 'GET':
        xCoord = int(request.args['x'])
        yCoord = int(request.args['y'])
    else: return {'status': 'error'}
    
    # First check if there are any empty cells
    if ((not checkForEmptyCells()) or (gameOver == True) or (moveCounter <= 0)):
        # Board is full, so set gameOver to true
        gameOver = True
        # Calculate the winner and retrun the results
        return determineWinner()
    
    # If the ai opponent is active and it is its turn, get it to make a move
    if (aiOpponentToggle == True and currentPlayer == "Light"):
        # Delay so the other player can see where they placed their own counter
        time.sleep(1)

        # Ask the ai which move it will make
        ai_move = aio.makeMove(board)

        # Check if the ai could find a move
        if ai_move == (-1, -1):
            # The AI has no legal moves. Check if  dark has any moves.
            if not any_legal_moves("Dark ", board):
                # Neither player can move. Game Over.
                gameOver = True
                return determineWinner()
            
            # If dark can still move, pass the turn to them
            currentPlayer = "Dark "
            return {
                'status': 'no_legal_moves',
                'player': currentPlayer
            }
        
        # AI can make a move, so make the move
        isLegalMove = comp.legal_move(currentPlayer, ai_move, board, True)
        if (not isLegalMove): 
            # Inform the player that this is not a legal move
            return {
                'status': 'fail',
                'message': 'illegal move'
            }
        
        # Check if there are any free spaces
        if (not checkForEmptyCells()): return determineWinner()
        
        # Otherwise, switch to other player
        currentPlayer = "Dark "

        # Decrement the move counter
        moveCounter -= 1
        
        # Return the success status and the new state of the board
        return {
            'status': 'success',
            'board': board.tolist(),
            'player': currentPlayer
        }
    else:
        # Check if there are any legal moves available for the current player
        if (not any_legal_moves(currentPlayer, board)):
            # Determine the other player
            if (currentPlayer == "Dark "): otherPlayer = "Light"
            else: otherPlayer = "Dark "

            # Check whether either player can make a move
            if (not any_legal_moves(otherPlayer, board)):
                # Therefore, game is over
                gameOver = True
                return determineWinner()

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
        
        # Check if there are any free spaces
        if (not checkForEmptyCells()): return determineWinner()
        
        # Otherwise, switch to other player
        if (currentPlayer == "Dark "): currentPlayer = "Light"
        else: currentPlayer = "Dark "

        # Decrement the move counter
        moveCounter -= 1
        
        # Return the success status and the new state of the board
        return {
            'status': 'success',
            'board': board.tolist(),
            'player': currentPlayer
        }
