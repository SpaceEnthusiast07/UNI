import Data.List((\\))

generator2 :: [(Int,Int)]
generator2
    = [(read [tp1,tp2,tp3,tp4], read [cp1,cp2,cp3,cp4])
    | tp1 <- d
    , tp2 <- d
    , tp3 <- d
    , tp4 <- d
    , cp1 <- d \\ [tp1,tp2,tp3,tp4]
    , cp2 <- d \\ [tp1,tp2,tp3,tp4,cp1]
    , cp3 <- d \\ [tp1,tp2,tp3,tp4,cp1,cp2]
    , cp4 <- d \\ [tp1,tp2,tp3,tp4,cp1,cp2,cp3]
    , cp1 > cp2 && cp2 > cp3 && cp3 > cp4
    ]
    where
    d = "123456789"

main :: IO ()
main = print (length generator2)