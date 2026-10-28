# Q4 The Odd One Out

George drew a 3x3 grid and wrote an odd digit in each cell.

Martha did the same and the grids are equal except one cell.

Both grids contain 8 different 3-digit prime numbers:
 - 1 in each row, reading from left to right
 - 1 in each column, reading from top to bottom
 - 1 in each diagonal, reading from top corner to bottom corner

All 8 of George's primes are also primes in reverse.

Only 7 of Martha's primes are primes in reverse.

**Question:** Which prime in Martha's grid is not a prime in reverse?

**Answer:** $173$.


<br>

## Generator
Returns a list of numbers represented as strings.

Each number:
 - has 3 odd digits
 - is prime
 - is not prime in reverse


<br>

## Selector
Steps:
    - Write a function to generate all 3x3 grids that contain 8 different 3-digit double primes that consist of odd digits only; i.e., generate all possible grids that are George's grid.
    - This function should only output 2 grids, so hardcode this into another function, so that this new function simply returns these two hardcoded grids.
    - Write a function that generates all 3x3 grids that have 8 prime 3-digit numbers, only 7 of them are prime when read backwards, consist of only odd digits, and is identical to any of George's grids except for one cell; i.e., generate all possible grid that are Martha's grid.
    - This function should output 2 grids, so hardcode these into a new function as well.
    - Finally, write a function that tests whether the provided number is within one of Martha's grids.
