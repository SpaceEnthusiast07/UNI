# Q2 Hidden PINs

Bank given Richard:
 - Telephone PIN
 - Debit card PIN
 - Both 4 digits

Telephone PIN is a perfect square.

Square root of telephone PIN is last 2 digits of card PIN.

Card PIN has no repeating digits.

Card PIN digits are in decreasing order.

Card PIN has no digits from telephone PIN.

Telephone PIN has a repeated digit.

**Question:** What is the card PIN?

**Answer:** 9762


<br>

## Generator
 - Generate a list of 2-tuples: $(C,T)$
 - $C$ is the debit card pin: digits are $(c1,c2,c3,c4)$
     - No repeating digits
     - Digits in decreasing order - use $>$ instead of $\geq$ to ensure no repeating digits
 - $T$ is the telephone pin: digits are $(t1,t2,t3,t4)$
     - Doesn't contain any digits from $C$


<br>

## Selector
 - Calculate the square of the last two digits of $C$
 - Check if equal to $T$


<br>

## Final Program
```Haskell
import Data.List((\\))

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

last2Digits :: String -> Int
last2Digits (x1:x2:x3:x4:xs)
    = read [x3,x4]

selector2 :: (String,String) -> Bool
selector2 (c,t)
    = (read t) == s*s
    where
    s = last2Digits (c)

main :: IO ()
main = print (filter selector2 generator2)
```

**Output:** `[("7653","2809"),("8754","2916"),("9762","3844")]`

Since the teaser says that "If I told you that the telephone PIN has a repeated digit, you will be able to work out both PINs".

Therefore, the correct pair is: `("9762","3844")`
 - Debit card PIN = $9762$
 - Telephone PIN = $3844$