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

Since George's grid is not linked in any way to Martha's, we do not need to consider George's grid at all.


<br>

## Generator
Returns a list of numbers represented as strings.

Each number:
 - has 3 odd digits
 - is prime
 - is not prime in reverse


<br>

## Selector
