{-
    - Determines if the provided integer is prime
-}
isPrime :: Int -> Bool
isPrime n
    = factors n == [1,n]
    where
    factors n
        = [f | f <- [1..n], n `mod` f == 0]

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
    , d2 <- (oddDigits ++ ['0'])
    , d3 <- oddDigits
    -- Ensure num is prime
    , isPrime (read [d1,d2,d3])
    -- Ensure num is not prime in reverse
    , isPrime (read [d3,d2,d1]) == False
    ]
    where
    oddDigits = "13579"




main :: IO ()
main = print (generator4)





x_generator4 :: Int
x_generator4
    = length [t | t <- [t1,t2,t3,t4,t5], t]
    where
    t1 = "331" `elem` generator4
    t2 = "557" `elem` generator4
    t3 = "593" `elem` generator4
    t4 = "151" `notElem` generator4
    t5 = "991" `notElem` generator4