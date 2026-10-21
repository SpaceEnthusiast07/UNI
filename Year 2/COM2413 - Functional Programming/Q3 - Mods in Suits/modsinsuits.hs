import Data.List((\\))

{-
    - Determines the modified value of the provided card
    - In the case of Diamond being the suit, the second card is used
    (right element in hand tuple)
    - s = suit; fv = face value
-}
score :: ((Char,Int),(Char,Int)) -> Int
score ((s1,fv1),(s2,fv2))
    = case s1 of
    'S' -> fv1 * fv1
    'H' -> fv1 `div` 2
    'C' -> -1 * fv1
    'D' -> fv1 `div` fv2

{-
    - "js1" refers to the suit of Jo's 1st card
    - "bv2" refers to the value of Bo's 2nd card
-}
generator3 :: [(((Char,Int),(Char,Int)),((Char,Int),(Char,Int)))]
generator3
    = [(((js1,jv1),(js2,jv2)),((bs1,bv1),(bs2,bv2)))
    | js1 <- suits
    , jv1 <- values
    , js2 <- suits \\ [js1]
    , jv2 <- values
    , (score ((js1,jv1),(js2,jv2))) + (score ((js2,jv2),(js1,jv1))) > 0
    , bs1 <- suits \\ [js1,js2]
    , bv1 <- values
    , bs2 <- suits \\ [js1,js2,bs1]
    , bv2 <- values
    , (score ((bs1,bv1),(bs2,bv2))) + (score ((bs2,bv2),(bs1,bv1))) < 0
    ]
    where
    suits = "CDHS"
    values = [1..13]


x_generator3 :: Int
x_generator3
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = ((('D',6) ,('H',2)),(('C',5),('S',1))) `elem` generator3
    t2 = ((('D',10),('H',2)),(('C',7),('S',1))) `elem` generator3
    t3 = ((('S',1),('D',6)),(('C',9),('H',4))) `elem` generator3
    t4 = ((('S',2),('D',8)),(('C',10),('H',4))) `elem` generator3
    t5 = ((('D',6),('S',1)),(('C',13),('H',12))) `elem` generator3

selector3 :: (((Char,Int),(Char,Int)),((Char,Int),(Char,Int))) -> Bool
selector3 (((js1,jv1),(js2,jv2)),((bs1,bv1),(bs2,bv2)))
    = 


main :: IO ()
main = print (x_generator3)