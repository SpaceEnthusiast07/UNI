import Data.List((\\))

{-
    - Determines if the provided integer is prime
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


genGeorgesGrids :: String -> Bool
genGeorgesGrids [n1,n2,n3]
    = length [[c1,c2,c3
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
    -- Ensure the 8 numbers are prime when read forwards
    ,  isPrime (read [c1,c2,c3]) && isPrime (read [c4,c5,c6]) && isPrime (read [c7,c8,c9])
    && isPrime (read [c1,c4,c7]) && isPrime (read [c2,c5,c8]) && isPrime (read [c3,c6,c9])
    && isPrime (read [c1,c5,c9]) && isPrime (read [c3,c5,c7])
    -- 
    ,  (length ([c1,c2,c3] \\ [n1,n2,n3])) == 0
    || (length ([c4,c5,c6] \\ [n1,n2,n3])) == 0
    || (length ([c7,c8,c9] \\ [n1,n2,n3])) == 0
    || (length ([c1,c4,c7] \\ [n1,n2,n3])) == 0
    || (length ([c2,c5,c8] \\ [n1,n2,n3])) == 0
    || (length ([c3,c6,c9] \\ [n1,n2,n3])) == 0
    || (length ([c1,c5,c9] \\ [n1,n2,n3])) == 0
    || (length ([c3,c5,c7] \\ [n1,n2,n3])) == 0
    -- Check if each num is not prime backwards, if so, is it the number in question
    , length [t 
        | let t1 = if (not (isPrime (read [c3,c2,c1]))) then [c1,c2,c3] == [n1,n2,n3] else False
        , let t2 = if (not (isPrime (read [c6,c5,c4]))) then [c4,c5,c6] == [n1,n2,n3] else False
        , let t3 = if (not (isPrime (read [c9,c8,c7]))) then [c7,c8,c9] == [n1,n2,n3] else False
        , let t4 = if (not (isPrime (read [c7,c4,c1]))) then [c1,c4,c7] == [n1,n2,n3] else False
        , let t5 = if (not (isPrime (read [c8,c5,c2]))) then [c2,c5,c8] == [n1,n2,n3] else False
        , let t6 = if (not (isPrime (read [c9,c6,c3]))) then [c3,c6,c9] == [n1,n2,n3] else False
        , let t7 = if (not (isPrime (read [c9,c5,c1]))) then [c1,c5,c9] == [n1,n2,n3] else False
        , let t8 = if (not (isPrime (read [c7,c5,c3]))) then [c3,c5,c7] == [n1,n2,n3] else False
        , t <- [t1,t2,t3,t4,t5,t6,t7,t8]
        , t
        ] == 1
    ] > 0
    where
    oddDigits = "1379"


selector4 :: String -> Bool
selector4 [n1,n2,n3]
    = length [[d1,d2,d3]
    | d1 <- oddDigits
    , d2 <- oddDigits
    , d3 <- oddDigits \\ ['5']
    -- Ensure num is prime
    , isPrime (read [d1,d2,d3])
    -- Ensure num is prime in reverse
    , isPrime (read [d3,d2,d1])
    ,  (n1 == d1 && n2 == d2)
    || (n1 == d1 && n3 == d3)
    || (n2 == d2 && n3 == d3)
    ] == 3
    where
    oddDigits = "13579"


main :: IO ()
-- main = print (filter selector4 generator4)
main = print (genGeorgesGrids "173")
-- main = print (length generator4)












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