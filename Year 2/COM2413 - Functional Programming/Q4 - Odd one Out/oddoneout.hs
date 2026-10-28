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
    - Generats a list of integers represented as strings, such that each integer:
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
    - Returns all possible 3x3 grids with 8 different double primes; i.e.,
    George's grids.
-}
georgesGrids :: [String]
georgesGrids = ["113751971","179157311"]

{-
    - Returns all possible 3x3 grids that contain 8 different 3-digit primes,
    only 7 of them are prime when read backwards, and are identical to any of
    George's grids except for one cell; i.e., Martha's grids.
-}
marthasGrids :: [String]
marthasGrids = ["173751971","179757311"]

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
    - Selects numbers that can be inserted into one of Martha's possible grid.
-}
selector4 :: String -> Bool
selector4 [n1,n2,n3]
    = length [marthasGrid
    | marthasGrid <- marthasGrids
    , canInsertNum [n1,n2,n3] marthasGrid
    ] > 0

main :: IO ()
main = print (filter selector4 generator4)