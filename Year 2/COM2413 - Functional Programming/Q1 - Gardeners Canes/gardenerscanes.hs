{-
    - Selects tuples of 4 Ints, one for each of the broken pieces of the 2 broken 98-inch canes.
    - Each length cannot be 0 or 98 as this would imply a cane is not broken.
    - The 4 lengths are ordered to aid the selecting process and each pair must sum to 98 to make a full cane.
-}
generator1 :: [(Int,Int,Int,Int)]
generator1
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

{-
    - Calculates area of triangle formed using two broken cane pieces and one 70-inch cane, using Heron's formula.
    - "fromIntegral" is used to convert "s*...*(s-c)" to a float as "sqrt" only takes floats.
    - "`div`" is used because the standard division operator "/" only works on floats.
-}
triArea :: Int -> Int -> Int -> Float
triArea a b c
    = sqrt (fromIntegral (s*(s-a)*(s-b)*(s-c)))
    where
    s = (a+b+c) `div` 2

{-
    - Only selects broken cane lengths where their respective triangle areas differ by exactly 504 square-inches.
    - "abs" is used to ensure area difference is positive.
-}
selector1 :: (Int,Int,Int,Int) -> Bool
selector1 (a,b,c,d)
    = abs(triDiff) == 504
    where
    triDiff = triArea a b 70 - triArea c d 70

-- filter is used to only output the tuple of lengths the selector determines that conforms to the constraints.
main :: IO ()
main = print(filter selector1 generator1)
