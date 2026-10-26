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
Generate a list of all 3-digit numbers of only odd digits that are prime and prime in reverse.

Could use list difference to see if replacing 1 digit from any of the 8 fancy primes would result in only 7 fancy primes.