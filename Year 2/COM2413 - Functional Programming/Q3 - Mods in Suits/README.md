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
Since Haskell doesn't have structures or classes, the idea of a card, hand, and game are purely conceptual.

The list the generator returns will be: ($game$-($hand$-($card$,$card$), $hand$-($card$,$card$))) structure.


<br>

## Selector
Given a FINAL game, determine if a middle game (BEFORE exchanging second card) exists such that:
 - the overall player score is unchanged
 - the initial game has all different suits and values
 - the final game has all different suits

<br>

> [!NOTE]
> Since only the second card is changed and all the suits are still different, that means Jo and Bo simply swap second card suits!

Selector input: `((jo_final_hand),(bo_final_hand))`. `jo_final_hand.card_1` and `bo_final_hand.card_1` remain unchanged. Jo and Bo swap thier `card_2.suit`.

Initial draw: `(((jis1,jiv1),(jis2,jiv2)),((bis1,biv1),(bis2,biv2)))`.
 - `j` = Jo
 - `b` = Bo
 - `i` = initial
 - `s` = suit
 - `v` = value
 - `1` = first card
 - `2` = second card

Since first cards stay the same and second card's suits are swapped, final game: `(((jis1,jiv1),(bis2,jfv2)),((bis1,biv1),(jis2,bfv2)))`.
 - `f` = final

We want:
 - `handScore ((jis1,jiv1),(jis2,jiv2)) == handScore ((jis1,jiv1),(bis2,jfv2))`
 - `handScore ((bis1,biv1),(bis2,biv2)) == handScore ((bis1,biv1),(jis2,bfv2))`

We know everything except for `jiv2` and `biv2`.

**Selector Steps:**
1. Calculate initial second cards values for both Jo and Bo based on initial first card and swapped second card suit, such that the hand value is unchanged.
2. Ensure this value is between 1 and 13, inclusive.
3. Ensure all initial card values are different.