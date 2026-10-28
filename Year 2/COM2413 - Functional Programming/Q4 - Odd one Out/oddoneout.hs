import Data.List((\\))

{-
    - Determines if the provided integer is prime.
-}
isPrime :: Int -> Bool
isPrime n
    = factors n == [1,n]
    where
    factors n
        = [f | f <- [1..sn], n `mod` f == 0] ++ [n]
        where
        sn = (floor (sqrt (fromIntegral n)))

{-
    - Determines if the provided 3-digit number, represented as a string,
    is prime when read forwards and backwards.
-}
isDoublePrime :: String -> Bool
isDoublePrime [d1,d2,d3]
    =  isPrime (read [d1,d2,d3])
    && isPrime (read [d3,d2,d1])

{-
    - Generats a list of integers represented as strings, such that each number:
    - has 3 odd digits
    - is prime
    - is not prime in reverse
-}
generator4 :: [String]
generator4
    = [[d1,d2,d3]
    | d1 <- oddDigits
    , d2 <- oddDigits
    , d3 <- oddDigits \\ ['5']
    -- Ensure num is prime
    , isPrime (read [d1,d2,d3])
    -- Ensure num is not prime in reverse
    , isPrime (read [d3,d2,d1]) == False
    ]
    where
    oddDigits = "13579"

{-
    - Returns a list of all 3-digit integers that are primes when read
    forwards and backwards, and consist of only odd digits.
-}
genDoublePrimes :: [String]
genDoublePrimes
    = ["113","131","179","191","199","151","157","311"
      ,"313","337","373","353","359","733","739","797"
      ,"751","757","919","937","971","991","953"]

{-
    --- DEPRECIATED ---
    - Generates all possible 3x3 grids that contain 8 different double primes.
-}
genGeorgesGrids :: [String]
genGeorgesGrids
    = [[c1,c2,c3
       ,c4,c5,c6
       ,c7,c8,c9]
    | c1 <- oddDigits
    , c2 <- oddDigits
    , c3 <- oddDigits
    , c4 <- oddDigits
    , c5 <- oddDigits ++ ['5']
    , c6 <- oddDigits
    , c7 <- oddDigits
    , c8 <- oddDigits
    , c9 <- oddDigits
    , length (genDoublePrimes \\ [[c1,c2,c3],[c4,c5,c6],[c7,c8,c9],[c1,c4,c7],[c2,c5,c8],[c3,c6,c9],[c1,c5,c9],[c3,c5,c7]]) == 15
    ,  isDoublePrime [c1,c2,c3] && isDoublePrime [c4,c5,c6] && isDoublePrime [c7,c8,c9]
    && isDoublePrime [c1,c4,c7] && isDoublePrime [c2,c5,c8] && isDoublePrime [c3,c6,c9]
    && isDoublePrime [c1,c5,c9] && isDoublePrime [c3,c5,c7]
    ]
    where
    oddDigits = "1379"

{-
    - Returns all possible 3x3 grids with 8 different double primes; i.e.,
    George's grids.
-}
georgesGrids :: [String]
georgesGrids = ["113751971","179157311"]

{-
    --- DEPRECIATED ---
    - Generates all possible 3x3 grids that contain 8 different 3-digit primes
    and only 7 of them are prime when read backwards.
-}
genMarthasGrids :: [String]
genMarthasGrids
    = [[c1,c2,c3
       ,c4,c5,c6
       ,c7,c8,c9]
    | c1 <- oddDigits
    , c2 <- oddDigits
    , c3 <- oddDigits
    , c4 <- oddDigits
    , c5 <- oddDigits ++ ['5']
    , c6 <- oddDigits
    , c7 <- oddDigits
    , c8 <- oddDigits
    , c9 <- oddDigits
    -- Ensure there are only 7 DIFFERENT double primes
    , length (genDoublePrimes \\ [[c1,c2,c3],[c4,c5,c6],[c7,c8,c9],[c1,c4,c7],[c2,c5,c8],[c3,c6,c9],[c1,c5,c9],[c3,c5,c7]]) == 16
    -- Ensure all 8 numbers are prime when read forwards
    ,  isPrime (read [c1,c2,c3]) && isPrime (read [c4,c5,c6]) && isPrime (read [c7,c8,c9])
    && isPrime (read [c1,c4,c7]) && isPrime (read [c2,c5,c8]) && isPrime (read [c3,c6,c9])
    && isPrime (read [c1,c5,c9]) && isPrime (read [c3,c5,c7])
    -- Ensure there are only 7 numbers that are prime when read backwards
    , length [reversePrimes
        | let n1 = isPrime (read [c3,c2,c1])
        , let n2 = isPrime (read [c6,c5,c4])
        , let n3 = isPrime (read [c9,c8,c7])
        , let n4 = isPrime (read [c7,c4,c1])
        , let n5 = isPrime (read [c8,c5,c2])
        , let n6 = isPrime (read [c9,c6,c3])
        , let n7 = isPrime (read [c9,c5,c1])
        , let n8 = isPrime (read [c7,c5,c3])
        , reversePrimes <- [n1,n2,n3,n4,n5,n6,n7,n8]
        , reversePrimes
        ] == 7
    ]
    where
    oddDigits = "1379"

{-
    - Returns all possible 3x3 grids that contain 8 different 3-digit primes,
    only 7 of them are prime when read backwards, and are identical to any of
    George's grids except one cell; i.e., Martha's grids.
-}
marthasGrids :: [String]
marthasGrids = ["173751971","179757311"]

{-
    - Determines if two grids are identical except for one cell.
-}
areCompatibleGrids :: String -> String -> Bool
areCompatibleGrids [g1,g2,g3,g4,g5,g6,g7,g8,g9] [m1,m2,m3,m4,m5,m6,m7,m8,m9]
    = length [t | t <- [t1,t2,t3,t4,t5,t6,t7,t8,t9], t] == 8
    where
    t1 = g1 == m1
    t2 = g2 == m2
    t3 = g3 == m3
    t4 = g4 == m4
    t5 = g5 == m5
    t6 = g6 == m6
    t7 = g7 == m7
    t8 = g8 == m8
    t9 = g9 == m9

{-
    - Determines if the provided prime is one of the 8 primes in the provided 3x3 grid.
-}
canInsertNum :: String -> String -> Bool
canInsertNum num [c1,c2,c3
                 ,c4,c5,c6
                 ,c7,c8,c9]
    = length [t | t <- [t1,t2,t3,t4,t5,t6,t7,t8], t] == 1
    where
    t1 = num == [c1,c2,c3]
    t2 = num == [c4,c5,c6]
    t3 = num == [c7,c8,c9]
    t4 = num == [c1,c4,c7]
    t5 = num == [c2,c5,c8]
    t6 = num == [c3,c6,c9]
    t7 = num == [c1,c5,c9]
    t8 = num == [c3,c5,c7]

{-
    - Selects numbers that can be inserted into Martha's grid,
    given Martha's grid is identical to George's except for one cell
-}
selector4 :: String -> Bool
selector4 [n1,n2,n3]
    = length [marthasGrid
    | marthasGrid <- marthasGrids
    , canInsertNum [n1,n2,n3] marthasGrid
    ] > 0

main :: IO ()
main = print (filter selector4 generator4)

{-
    TESTING FUNCTIONS
-}
x_generator4 :: Int
x_generator4
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = "331" `elem` generator4
    t2 = "557" `elem` generator4
    t3 = "593" `elem` generator4
    t4 = "151" `notElem` generator4
    t5 = "991" `notElem` generator4

x_selector4 :: Int
x_selector4
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = selector4 "193" == False
    t2 = selector4 "397" == False
    t3 = selector4 "557" == False
    t4 = selector4 "911" == False
    t5 = selector4 "997" == False