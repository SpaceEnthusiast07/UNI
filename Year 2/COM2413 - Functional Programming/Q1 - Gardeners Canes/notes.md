# Q1 Gardener's Canes


Initially, gardener has:
 - x2 70-inch long bamboo canes
 - x2 98-inch long bamboo canes

Wife breaks both 98-inch ones with car, then:
 - each break into 2 pieces (not equal), totaling 4 pieces now
 - each piece is a whole number of inches long

Now, of 4 broken pieces:
 - triangle is formed by connecting longest and shortest to 70-inch cane
     - longest and shortest broken pieces come from same cane
 - triangle is also formed by connecting both medium pieces to other 70-inch cane
     - both medium come from same cane

Then,
 - triangle areas differ by 504 inches

<strong>Question: What is the length of the shortest cane?</strong>


<br>

## Generator
Generate 4 numbers, $(A,B,C,D)$ in a tuple, one for the length of each broken cane piece.

Lengths $A$ and $B$ are from one 98-inch cane, and $C$ and $D$ are from the other 98-inch cane, such that:
 - $1 \leq A \leq B \leq 97$
 - $1 \leq C \leq D \leq 97$


<br>

## Selector
...
