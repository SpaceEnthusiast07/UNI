# Technical Breakdown of Othello

In this document I explain how the different modules work and why I choose their respective approach. Each explanation is accompanied by a flowchart of the algorithm used.

[//]: <> (Add table of contents)

## Module 1: `components.py`
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


## Module 2
### Function 1
### Function 2
