import Data.List((\\))

{-
    - Generates a list of 2-tuples: (C,T).
    - C is the debit card pin with no repeating digits and are in decreasing order.
    - T is the telephone pin that doesn't contain any digits from C.
    - Having '0' as the start digit would imply a 3 digit number not a 4 digit one.
-}
generator2 :: [(String,String)]
generator2
    = [([c1,c2,c3,c4], [t1,t2,t3,t4])
    | c1 <- d \\ ['0']
    , c2 <- d \\ [c1]
    , c3 <- d \\ [c1,c2]
    , c4 <- d \\ [c1,c2,c3]
    , c1 > c2 && c2 > c3 && c3 > c4
    , t1 <- d \\ ['0',c1,c2,c3,c4]
    , t2 <- d \\ [c1,c2,c3,c4]
    , t3 <- d \\ [c1,c2,c3,c4]
    , t4 <- d \\ [c1,c2,c3,c4]
    ]
    where
    d = "0123456789"

{-
    - Given a String representation of a 4 digit number, returns the last 2 digits.
-}
last2Digits :: String -> Int
last2Digits (x1:x2:x3:x4:xs)
    = read [x3,x4]

{-
    - Selects the card-telephone pin tuple where squaring the last two digits of the
    card pin equals the telephone pin.
-}
selector2 :: (String,String) -> Bool
selector2 (c,t)
    = (read t) == s*s
    where
    s = last2Digits (c)

main :: IO ()
main = print (filter selector2 generator2)