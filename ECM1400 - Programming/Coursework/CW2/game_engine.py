import components as comp
import os, platform, time

# Function that aks user for coordinates to place a counter, then formats them
def cli_coords_input():
    validCoordinates = False
    while not validCoordinates:
        # Ask the user for the x and y coordinate
        userXInput = input("Enter x-coord: ")
        userYInput = input("Enter y-coord: ")

        # Check if they have inputted an integer for x and y
        try:
            # Convert both coordinates to integers
            xCoord = int(userXInput)
            yCoord = int(userYInput)

            validCoordinates = True

            # Format and return the coordinate tuple
            return (xCoord, yCoord)
        except:
            # Inform the user that these are invalid coordinates
            print("Invalid coordinates!")


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
    

# Main loop for game
def simple_game_loop():
    # Initialise the board
    board = comp.initialise_board()

    # Initialise the move counters
    moveCounter = 60
    lightCounter = 0
    darkCounter = 0

    # Initialise legalMovePossible and noLegalMoveCounter
    legalMovePossible = True
    noLegalMoveCounter = 0

    # Set the starting player
    currentPlayer = "Dark "

    # Loop through each player's turn
    while legalMovePossible and moveCounter > 0:
        # Check which os this python file is on and clear the screen
        if (platform.system() == "Windows"): os.system("cls")
        else: os.system("clear")


        # Display welcome message
        print("=== Welcome to Reversi ===")
        
        # Display the board
        comp.print_board(board)

        # Check if there are any legal moves available for the current player
        if (not any_legal_moves(currentPlayer, board)):
            # Check whether either player can make a move
            if (noLegalMoveCounter == 2): 
                legalMovePossible = False
                break

            # Increment noLegalMoveCounter
            noLegalMoveCounter += 1

            # Switch to other player
            if (currentPlayer == "Dark "): currentPlayer = "Light"
            else: currentPlayer = "Dark "

            # Continue to next loop
            continue

        # Reset noLegalMoveCounter
        noLegalMoveCounter = 0

        # Initialise legalMoveMade
        legalMoveMade = False

        print("-"*(len(board[0]) * 2 + 3))
        # Display which player's turn it is
        if (currentPlayer == "Dark "): print(f"{currentPlayer[:4]}'s turn")
        else: print(f"{currentPlayer}'s turn")

        # Allow the current player to keep placing counters until a legal move is made
        while not legalMoveMade:
            # Obtain the coordinates the current player is going to play
            coords = cli_coords_input()

            # Check whether the move is legal
            isLegalMove = comp.legal_move(currentPlayer, coords, board, True)
            if (not isLegalMove): 
                # Inform the player that this is not a legal move
                print("Not a legal move!\n")
                continue

            # Set legalMoveMade to True
            legalMoveMade = True
        
        # Increment the number of counters for the current player and move to the other player
        if (currentPlayer == "Dark "): 
            # Increment dark's counter
            darkCounter += 1
            # Move to light's turn
            currentPlayer = "Light"
        else: 
            # Increment light's counter
            lightCounter += 1
            # Move to dark's turn
            currentPlayer = "Dark "
        
        # Output legal move
        print("\nMove is legal!")
        time.sleep(2)
    
    # Print game over message and who won along with the counter stats
    print("-- GAME OVER --")
    # Check who won
    if (darkCounter > lightCounter): print("Dark Won!")
    else: print("Light Won!")
    # Output counter stats
    print(f"The board now contains:\n  -> {darkCounter} dark counters\n  -> {lightCounter} light counters")


if __name__ == "__main__":
    simple_game_loop()
