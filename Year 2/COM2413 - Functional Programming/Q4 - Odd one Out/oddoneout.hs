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


genDoublePrimes :: [String]
genDoublePrimes
    = [[d1,d2,d3]
    | d1 <- oddDigits
    , d2 <- oddDigits ++ ['5']
    , d3 <- oddDigits
    , isDoublePrime [d1,d2,d3]
    ]
    where
    oddDigits = "1379"


isGeorgesGrid :: String -> Bool
isGeorgesGrid [c1,c2,c3
              ,c4,c5,c6
              ,c7,c8,c9]
    =  isDoublePrime [c1,c2,c3] && isDoublePrime [c4,c5,c6]
    && isDoublePrime [c7,c8,c9] && isDoublePrime [c1,c4,c7]
    && isDoublePrime [c2,c5,c8] && isDoublePrime [c3,c6,c9]
    && isDoublePrime [c1,c5,c9] && isDoublePrime [c3,c5,c7]


isMarthasGrid :: String -> Bool
isMarthasGrid [c1,c2,c3
              ,c4,c5,c6
              ,c7,c8,c9]
    = length [t | t <- [n1,n2,n3,n4,n5,n6,n7,n8], t] == 7
    where
    n1 = isDoublePrime [c1,c2,c3]
    n2 = isDoublePrime [c4,c5,c6]
    n3 = isDoublePrime [c7,c8,c9]
    n4 = isDoublePrime [c1,c4,c7]
    n5 = isDoublePrime [c2,c5,c8]
    n6 = isDoublePrime [c3,c6,c9]
    n7 = isDoublePrime [c1,c5,c9]
    n8 = isDoublePrime [c3,c5,c7]


selector4 :: String -> Bool
selector4 [n1,n2,n3]
    = length [[d1,d2,d3]
    | d1 <- oddDigits
    , d2 <- oddDigits ++ ['5']
    , d3 <- oddDigits
    , isDoublePrime [d1,d2,d3]
    ,  (n1 == d1 && n2 == d2)
    || (n1 == d1 && n3 == d3)
    || (n2 == d2 && n3 == d3)
    ] >= 1
    where
    oddDigits = "1379"


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