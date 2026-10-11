
generator :: [(Int,Int,Int,Int)]
generator
    = [(a,b,c,d)
    | a <- t
    , b <- t
    , c <- t
    , d <- t
    , a < b && c < d && a < c
    , a + b == 98
    , c + d == 98
    ]
    where
    t = [1..97]

triArea :: Int -> Int -> Int -> Float
triArea a b c
    = sqrt (fromIntegral (s*(s-a)*(s-b)*(s-c)))
    where
    s = (a+b+c) `div` 2

selector :: (Int,Int,Int,Int) -> Bool
selector (a,b,c,d)
    = abs(triDiff) == 504
    where
    triDiff = triArea a b 70 - triArea c d 70

main :: IO ()
main = print(filter selector generator)