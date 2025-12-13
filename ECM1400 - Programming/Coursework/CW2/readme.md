# Technical Breakdown of Othello

In this document I explain how each module works and why I choose their respective approach. Each function is accompanied by a flowchart of the algorithm used.


Table of Contents
- [Technical Breakdown of Othello](#technical-breakdown-of-othello)
  - [Module 1 - `components.py`](#module-1---componentspy)
    - [Function Descriptions](#function-descriptions)
      - [1. initialise\_board(size: int = 8):](#1-initialise_boardsize-int--8)
      - [2. print\_board(board: list\[list\[str\]\]):](#2-print_boardboard-listliststr)
      - [3. legal\_move(colour: str, coordinate: tuple, board: list\[list\[str\]\], modify\_board: bool):](#3-legal_movecolour-str-coordinate-tuple-board-listliststr-modify_board-bool)
  - [Module 2 - `ai_opponent.py`](#module-2---ai_opponentpy)
    - [Function Descriptions](#function-descriptions-1)
      - [Function 1](#function-1)
      - [Function 2](#function-2)


## Module 1 - `components.py`
This module contains three utility functions that provide the
functionality for the Othello/Reversi game to work.

Typical import:

```import components as comp```


Public Functions:
 - initialise_board()
 - print_board()
 - legal_move()

Internal Helper Functions:
 - _analyse_cell()


### Function Descriptions
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


## Module 2 - `ai_opponent.py`



### Function Descriptions
#### Function 1



#### Function 2



