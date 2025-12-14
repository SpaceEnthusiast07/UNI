# Technical Breakdown of Othello

In this document I explain how each module works and why I choose their respective approach. Each function is accompanied by a flowchart of the algorithm used.


Table of Contents
- [Technical Breakdown of Othello](#technical-breakdown-of-othello)
  - [Module 1 - `components.py`](#module-1---componentspy)
      - [1. initialise\_board(size: int = 8):](#1-initialise_boardsize-int--8)
      - [2. print\_board(board: list\[list\[str\]\]):](#2-print_boardboard-listliststr)
      - [3. legal\_move(colour: str, coordinate: tuple, board: list\[list\[str\]\], modify\_board: bool):](#3-legal_movecolour-str-coordinate-tuple-board-listliststr-modify_board-bool)
      - [4. \_analyse\_cell(colour: str, cell\_to\_check: object, board: object, direction: object, modify\_board: bool):](#4-_analyse_cellcolour-str-cell_to_check-object-board-object-direction-object-modify_board-bool)
  - [Module 2 - `ai_opponent.py`](#module-2---ai_opponentpy)
      - [1. calculate\_move(board: list\[list\[str\]\]):](#1-calculate_moveboard-listliststr)
      - [2. \_legal\_move(ai\_colour: str, coordinate: tuple, board: list\[list\[str\]\]):](#2-_legal_moveai_colour-str-coordinate-tuple-board-listliststr)
      - [3. \_analyse\_cell(ai\_colour: str, cell\_to\_check: tuple, board: list\[list\[str\]\], direction: tuple, board\_size: int):](#3-_analyse_cellai_colour-str-cell_to_check-tuple-board-listliststr-direction-tuple-board_size-int)
  - [Module 3 - `game_engine.py`](#module-3---game_enginepy)
      - [1. simple\_game\_loop():](#1-simple_game_loop)
      - [2. \_cli\_coords\_input():](#2-_cli_coords_input)
      - [3. \_any\_legal\_moves(colour: str, board: object):](#3-_any_legal_movescolour-str-board-object)
  - [Module 4 - `flask_game_engine.py`](#module-4---flask_game_enginepy)
      - [1. home\_page():](#1-home_page)
      - [2. move():](#2-move)
      - [3. send\_game\_state\_to\_user():](#3-send_game_state_to_user)
      - [4. load\_user\_saved\_game\_state\_bytes():](#4-load_user_saved_game_state_bytes)
      - [5. reset\_board():](#5-reset_board)
      - [6. toggle\_ai\_opponent():](#6-toggle_ai_opponent)
      - [7. \_any\_legal\_moves(colour: str, board: list\[list\[str\]\]):](#7-_any_legal_movescolour-str-board-listliststr)
      - [8. \_save\_game\_state\_to\_file(current\_game\_state: dict):](#8-_save_game_state_to_filecurrent_game_state-dict)
      - [9. \_load\_game\_state\_from\_file():](#9-_load_game_state_from_file)
      - [10. \_load\_config\_data():](#10-_load_config_data)
      - [11. \_determine\_winner(board: list\[list\[str\]\]):](#11-_determine_winnerboard-listliststr)
      - [12. \_check\_for\_empty\_cells(board: list\[list\[str\]\]):](#12-_check_for_empty_cellsboard-listliststr)
      - [13. \_check\_for\_other\_players\_colour(colour: str, board: list\[list\[str\]\]):](#13-_check_for_other_players_colourcolour-str-board-listliststr)


## Module 1 - `components.py`
This module contains three utility functions that provide the
functionality for the Othello/Reversi game to work.

Typical import:
```import components as comp```

Half this module, `initialise_board()` and `print_board()`, wouldn't change much between developers however, `legal_move()` and `_analyse_cell()` would. I choose to use vectors and recursion within these two functions as it provided the functionality of travelling along multiple directions and backtracking along each direction to change the colour of a counter if required.

Public Functions:
 - initialise_board()
 - print_board()
 - legal_move()

Internal Helper Functions:
 - _analyse_cell()


#### 1. initialise_board(size: int = 8):
Creates a Reversi/Othello board of default size 8x8.
Then, sets up the centre four counters as follows:

```
|Light|Dark |
|Dark |Light|
```

This new board is returned as a regular 2d python list.
My algorihtm has been designed around a board with an even size and square shape,
so if the board's size is odd, e.g. `size=9`, `None` is returned.

Example Usage:
```board = comp.initialise_board(size=6)```


#### 2. print_board(board: list[list[str]]):
Prints a representation of the `board` to the console.
A *key* is displayed before the board to indicate what each symbol means.
Column and row numbers are displayed to make the process of reading the board easier.

Example Usage:
```comp.print_board(board)```


#### 3. legal_move(colour: str, coordinate: tuple, board: list[list[str]], modify_board: bool):
Given a player's `colour`, their chosen `coordinate`, the current state of the `board` and
whether the board should be *modified* or not, determine whether this move is legal,
based on the rules of Othello/Reversi.

Example:

```python
legal_move_result = comp.legal_move("Light", (6,7), board, True)
# Check if (6,7) is a legal move for player "Light"
if legal_move_result['is_legal_move'] is True:
    # Extract the new state of the board, only required if modify_board=True
    board = legal_move_result['board']
```


#### 4. _analyse_cell(colour: str, cell_to_check: object, board: object, direction: object, modify_board: bool):
This is the recursive function that travels along a particular direction to determine
if the current move is legal along this direction.

Returns True if legal and False if not.


## Module 2 - `ai_opponent.py`
This module houses all the functions required for the implementation
of an AI opponent in the Othello game.

Typical Import:
```import ai_opponent as aio```

Public Functions:
 - calculate_move()

Private Helper Functions:
 - _legal_move()
 - _analyse_cell()


#### 1. calculate_move(board: list[list[str]]):
Loops through each cell of the board and determines if any of the
empty cells are legal and how many counters each legal cell flips.

Each legal cell is added to a list containing the coordinate and
number of flipped counters. This list is then sorted using the number
of flipped counters as the key, in descending order.

The first coordinate is returned if only one exists, otherwise the
second is returned. If no legal moves are found, `(-1,-1)` is returned.

Example Usage:
```python
ai_move = aio.calculate_move(board)
# Check if the ai has not found a move
if ai_move == (-1,-1):
    # Report that the AI has not found a move
    print("AI has not found a move.")
```


#### 2. _legal_move(ai_colour: str, coordinate: tuple, board: list[list[str]]):
Given the AI's colour, an empty cell (`coordinate`), and the current state of the `board`,
determine whether this move is legal, based on the rules of Othello/Reversi.

If this move is legal, the number of flipped counters is counted along each direction.

A tuple is returned containing whether is move is legal along with the number of counters flipped.


#### 3. _analyse_cell(ai_colour: str, cell_to_check: tuple, board: list[list[str]], direction: tuple, board_size: int):
This is the recursive function that travels along the current direction to determine if the
AI can outflank the other player.

This function returns a tuple containing whether the direction resulted in an outflank and
the number of flipped counters.


## Module 3 - `game_engine.py`
This module is used to host the Othello game within the command line interface.

Typical Import:
```import game_engine```

Public Functions:
 - simple_game_loop()

Private Helper Functions:
 - _cli_coords_input()
 - _any_legal_moves()


#### 1. simple_game_loop():
This is the main function for the command line implementation of Othello/Reversi.

It deals with the logic behind verifying a move and ensuring the game can continue.

Once the game has ended, it calculates who is the winner, or if it is a draw, then
displayes the winner with the scores for each player.

Example Usage:
```game_engine.simple_game_loop()```


#### 2. _cli_coords_input():
This function aims to ask the current player for their chosen coordinates and contains
a loop for re-entering coordinates if they are invalid.


#### 3. _any_legal_moves(colour: str, board: object):
The purpose of this function is to determine if the specified colour player
has at least one legal move available, if so returns True, otherwise returns False.


## Module 4 - `flask_game_engine.py`
This module is used to host the Othello game using Flask (a python web server and framework)
and website GUI.

To use your own website GUI, replace the default `index.html` file within the `templates`
folder and ensure it is named `index.html`.

Typical Import:
```import flask_game_engine as fge```

To run the Flask server, use:
```fge.app.run()```

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