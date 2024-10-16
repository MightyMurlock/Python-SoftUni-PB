from math import floor, ceil

MAGNOLII_PRICE = 3.25
ZUMBULI_PRICE = 4
ROSI_PRICE = 3.5
CACTUSI_PRICE = 8
TAXES_PERCENTAGE = 5 / 100

magnolii_count = int(input())
zumbuli_count = int(input())
rosi_count = int(input())
cactusi_count = int(input())
gift_price = float(input())

total = ((magnolii_count * MAGNOLII_PRICE) +
         (zumbuli_count * ZUMBULI_PRICE) +
         (rosi_count * ROSI_PRICE) +
         (cactusi_count * CACTUSI_PRICE))
total -= total * TAXES_PERCENTAGE

if total < gift_price:
    print(f"She will have to borrow {ceil(gift_price - total)} leva.")
else:
    print(f"She is left with {floor(total - gift_price)} leva.")