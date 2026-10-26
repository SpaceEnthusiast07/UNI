import Data.List((\\))

{-
    - Determines the modified value of the provided card (1st tuple)
    - In the case of the suit being Diamond, the second card is used (2nd tuple)
    - s = suit; fv = face value; _f = float
-}
cardScore :: (Char,Int) -> (Char,Int) -> Float
cardScore (s1,fv1) (s2,fv2)
    = case s1 of
    'S' -> fv1_f * fv1_f
    'H' -> fv1_f / 2
    'C' -> -1 * fv1_f
    'D' -> fv1_f / fv2_f
    where
    fv1_f = fromIntegral fv1
    fv2_f = fromIntegral fv2

{-
    - Returns the score of a player's hand
    - Utilises cardScore function for each card
    - s = suit; fv = face value
-}
handScore :: (Char,Int) -> (Char,Int) -> Float
handScore (s1,fv1) (s2,fv2)
    = (cardScore (s1,fv1) (s2,fv2)) + (cardScore (s2,fv2) (s1,fv1))

{-
    - Determines if the provided float is an integer
-}
isInt :: Float -> Bool
isInt n
    = floor n == ceiling n

{-
    - Generator outputs final games
    - There must be 4 distinct suits present
    - Jo's score must be a positive integer
    - Bo's score must be the negative of Jo's and an integer
    - j = Jo; b = Bo; s = suit; v = face value; 1 = card 1; 2 = card 2
-}
generator3 :: [(((Char,Int),(Char,Int)),((Char,Int),(Char,Int)))]
generator3
    = [(((js1,jv1),(js2,jv2)),((bs1,bv1),(bs2,bv2)))
    -- Set up Jo's two final cards
    | js1 <- suits
    , jv1 <- values
    , js2 <- suits \\ [js1]
    , jv2 <- values
    -- Jo's score would be 0 if values are the same
    , jv1 /= jv2
    -- Improve code readability
    , let josScore = handScore (js1,jv1) (js2,jv2)
    -- Ensure Jo's score is a positive integer
    , (josScore > 0) && (isInt josScore)
    -- Set up Bo's two final cards
    , bs1 <- suits \\ [js1,js2]
    , bv1 <- values
    , bs2 <- suits \\ [js1,js2,bs1]
    , bv2 <- values
    -- Bo's score would be 0 if values are the same
    , bv1 /= bv2
    -- Improve code readability
    , let bosScore = handScore (bs1,bv1) (bs2,bv2)
    -- Ensure Bo's score is an integer
    , isInt bosScore
    -- Ensure Bo's score is the negative of Jo's
    , (-1 * bosScore) == josScore
    ]
    where
    suits = "SHCD"
    values = [1..13]

{-
    - Given the final second card and the initial second card's suit,
      calculate what the initial second card's value would have been
-}
calcInitialCard2Value :: ((Char,Int),(Char,Int)) -> Char -> Float
calcInitialCard2Value ((fs1,fv1),(fs2,fv2)) is2
    = case is2 of
    'S' -> sqrt (final_card_2_score)
    'H' -> 2 * final_card_2_score
    'C' -> -1 * final_card_2_score
    'D' -> (fromIntegral fv1) * final_card_2_score
    where
    final_card_2_score = cardScore (fs2,fv2) (fs1,fv1)

{-
    - Selects final games that have an initial game satisfying the following constraints:
    - All card values must be between 1 and 13 inclusive
    - Each player's score must be unchanged after exchanging second card
    - All initial card values must be different
    - f = final; i = initial; _f = float
-}
selector3 :: (((Char,Int),(Char,Int)),((Char,Int),(Char,Int))) -> Bool
selector3 (((jfs1,jfv1),(jfs2,jfv2)),((bfs1,bfv1),(bfs2,bfv2)))
    -- Ensure initial second card values are in the acceptable range
    =  jiv2_f >= 1 && jiv2_f <= 13
    && biv2_f >= 1 && biv2_f <= 13
    -- Ensure Jo's and Bo's initial second card values are integers
    && (isInt jiv2_f) && (isInt biv2_f)
    -- Ensure all the initial card values are different
    && (length ([1..13] \\ [jfv1,jiv2,bfv1,biv2])) == 9
    -- Ensure both Jo's and Bo's scores remain unchanged
    && (handScore (jfs1,jfv1) (bfs2,jiv2)) == (handScore (jfs1,jfv1) (jfs2,jfv2))
    && (handScore (bfs1,bfv1) (jfs2,biv2)) == (handScore (bfs1,bfv1) (bfs2,bfv2))
    -- Ensure Jo and Bo don't swap second card values when they exchange their second card
    && jfv2 /= biv2 && bfv2 /= jiv2
    where
    -- Calculate what Jo's and Bo's initial second card values would have been
    jiv2_f = calcInitialCard2Value ((jfs1,jfv1),(jfs2,jfv2)) bfs2
    biv2_f = calcInitialCard2Value ((bfs1,bfv1),(bfs2,bfv2)) jfs2
    -- Convert above values to integers
    jiv2 = floor jiv2_f
    biv2 = floor biv2_f

main :: IO ()
main = print (filter selector3 generator3)