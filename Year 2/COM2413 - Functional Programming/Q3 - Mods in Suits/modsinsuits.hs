import Data.List((\\))

{-
    - Determines the modified value of the provided card (1st tuple element)
    - In the case of Diamond being the suit, the second card is used (right element in hand tuple)
    - s = suit; fv = face value
-}
cardScore :: (Char,Int) -> (Char,Int) -> Int
cardScore (s1,fv1) (s2,fv2)
    = case s1 of
    'S' -> fv1 * fv1
    'H' -> fv1 `div` 2
    'C' -> -1 * fv1
    'D' -> fv1 `div` fv2



{-
    - Returns the score of a player's hand
    - Utilises score function for each card
    - s = suit; fv = face value
-}
handScore :: ((Char,Int),(Char,Int)) -> Int
handScore ((s1,fv1),(s2,fv2))
    = (cardScore (s1,fv1) (s2,fv2)) + (cardScore (s2,fv2) (s1,fv1))



isInt :: Float -> Bool
isInt x
    = floor x == ceiling x



{-
    - Generator outputs final games
    - "js1" refers to the suit of Jo's 1st card
    - "bv2" refers to the value of Bo's 2nd card
-}
generator3 :: [(((Char,Int),(Char,Int)),((Char,Int),(Char,Int)))]
generator3
    = [(((js1,jv1),(js2,jv2)),((bs1,bv1),(bs2,bv2)))
    -- Set up Jo's two final cards
    | js1 <- suits
    , jv1 <- values
    , js2 <- suits \\ [js1]
    , jv2 <- values
    -- Jo's score would be 0 if values the same
    , jv1 /= jv2
    -- Ensure Jo's score is positive
    , (handScore ((js1,jv1),(js2,jv2))) > 0
    -- Set up Bo's two final cards
    , bs1 <- suits \\ [js1,js2]
    , bv1 <- values
    , bs2 <- suits \\ [js1,js2,bs1]
    , bv2 <- values
    -- Bo's score would be 0 if values the same
    , bv1 /= bv2
    -- Bo's score is the negative of Jo's
    , (handScore ((bs1,bv1),(bs2,bv2))) == -1 * (handScore ((js1,jv1),(js2,jv2)))
    -- Ensure scores are whole numbers (ints)
    , if js1 == 'D' && (isInt ((fromIntegral jv1)/(fromIntegral jv2))) == False then False else True
    , if js1 == 'H' && (isInt ((fromIntegral jv1)/2)) == False then False else True
    , if js2 == 'D' && (isInt ((fromIntegral jv2)/(fromIntegral jv2))) == False then False else True
    , if js2 == 'H' && (isInt ((fromIntegral jv2)/2)) == False then False else True
    , if bs1 == 'D' && (isInt ((fromIntegral bv1)/(fromIntegral bv2))) == False then False else True
    , if bs1 == 'H' && (isInt ((fromIntegral bv1)/2)) == False then False else True
    , if bs2 == 'D' && (isInt ((fromIntegral bv2)/(fromIntegral bv2))) == False then False else True
    , if bs2 == 'H' && (isInt ((fromIntegral bv2)/2)) == False then False else True
    ]
    where
    suits = "CDHS"
    values = [1..13]



calcInitialCard2Value :: ((Char,Int),(Char,Int)) -> Char -> Int
calcInitialCard2Value ((fs1,fv1),(fs2,fv2)) is2
    = case is2 of
    'S' -> round (sqrt (fromIntegral (final_card_2_score)))
    'H' -> 2 * final_card_2_score
    'C' -> -1 * final_card_2_score
    'D' -> fv1 * final_card_2_score
    where
    final_card_2_score = cardScore (fs2,fv2) (fs1,fv1)



selector3 :: (((Char,Int),(Char,Int)),((Char,Int),(Char,Int))) -> Bool
selector3 (((jfs1,jfv1),(jfs2,jfv2)),((bfs1,bfv1),(bfs2,bfv2)))
    =  jiv2 >= 1 && jiv2 <= 13
    && biv2 >= 1 && biv2 <= 13
    && (length ([1..13] \\ [jfv1,bfv1,jiv2,biv2])) == 9
    && (handScore ((jfs1,jfv1),(bfs2,jiv2))) == (handScore ((jfs1,jfv1),(jfs2,jfv2)))
    && (handScore ((bfs1,bfv1),(jfs2,biv2))) == (handScore ((bfs1,bfv1),(bfs2,bfv2)))
    && jfv2 /= biv2 && bfv2 /= jiv2
    where
    jiv2 = calcInitialCard2Value ((jfs1,jfv1),(jfs2,jfv2)) bfs2
    biv2 = calcInitialCard2Value ((bfs1,bfv1),(bfs2,bfv2)) jfs2



main :: IO ()
main = print (filter selector3 generator3)






{-
    Testing functions
-}
x_generator3 :: Int
x_generator3
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = ((('D',6) ,('H',2)),(('C',5),('S',1))) `elem` generator3
    t2 = ((('D',10),('H',2)),(('C',7),('S',1))) `elem` generator3
    t3 = ((('S',1),('D',6)),(('C',9),('H',4))) `elem` generator3
    t4 = ((('S',2),('D',8)),(('C',10),('H',4))) `elem` generator3
    t5 = ((('D',6),('S',1)),(('C',13),('H',12))) `elem` generator3

x_selector3 :: Int
x_selector3
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = selector3 ((('D',7),('S',7)),(('C',1),('H',2))) == False
    t2 = selector3 ((('D',3),('H',3)),(('C',3),('S',3))) == False
    t3 = selector3 ((('S',1),('D',4)),(('C',7),('H',4))) == False
    t4 = selector3 ((('D',10),('H',2)),(('C',10),('S',2))) == False
    t5 = selector3 ((('D',2),('H',2)),(('C',13),('S',13))) == False
