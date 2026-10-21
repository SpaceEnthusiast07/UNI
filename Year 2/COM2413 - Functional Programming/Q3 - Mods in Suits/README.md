# Q3 Mods in Suits

Mods-in-suits is a single pack game; i.e, 52 cards.

Players are dealt 2 cards.

A card has a face $\text{value}$ from 1 (Ace) to 13 (King).

$\text{Value}$ modified by suit:
 - Spade = $\text{value} ^ {2}$
   - e.g. 3 of Spades = 9
 - Heart = $\text{value} / 2$
   - e.g. 6 of Hearts = 3
 - Club = $-1 * \text{value}$
   - e.g. 9 of Clubs = -9
 - Diamond = $\text{value1} / \text{value2}$
   - e.g. 12 of Diamonds and 6 of Spades = 2 for Diamond card

Players score sum of modified card values.

Player scores 0, if face values match.

Players can exchange second card for new card from pack.

**Scenario:**

Jo and Bo are playing Mods-in-Suits.

Jo's initial score was a positive integer.

Bo's initial score was a negative integer.

4 different suits and face values were dealt.

Both exchanged second card.

Score unchanged.

Suits were still all different.


<br>

## Representations
A $card$ is represented by a pair (2-tuple) consisting of:
 - a character for the *suit* (`'C'` for Clubs, `'D'` for Diamonds, `'H'` for Hearts, and `'S'` for Spades).
 - an integer for its *face value*: `1..13`

A $hand$ is represented by a pair (2-tuple) of $cards$.
 - Left = first card dealt
 - Right = second card dealt

A $game$ is represented by a pair (2-tuple) of $hands$.
 - Left = Jo's hand
 - Right = Bo's hand


<br>

## Generator
Since Haskell doesn't have structures or classes, the idea of a card, hand, and game are merely conceptual.

The list the generator returns will be: ($game$-($hand$-($card$,$card$), $hand$-($card$,$card$))).


<br>

## Selector
...


