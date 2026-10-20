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
 - Generate a list of 2-tuples.
 - First tuple value is the telephone pin, `tp`, comprised of `(tp1,tp2,tp3,tp4)`.
     - Any 4 digit number
 - Second tuple value is the card pin, `cp`, comprised of `(cp1,cp2,cp3,cp4)`.
     - Has no digits from `tp`
     - Own digits are in decreasing order


<br>

## Selector
...
