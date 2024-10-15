PUZZLE_PRICE = 2.6
DOLL_PRICE = 3
BEAR_PRICE = 4.1
MINION_PRICE = 8.2
TRUCK_PRICE = 2

SHOP_RENT_PERCENTAGE = 0.1

holiday_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_toys = (puzzle_count +
              doll_count +
              bear_count +
              minion_count +
              truck_count)

total_price = ((puzzle_count * PUZZLE_PRICE) +
               (doll_count * DOLL_PRICE) +
               (bear_count * BEAR_PRICE) +
               (minion_count * MINION_PRICE) +
               (truck_count * TRUCK_PRICE))

if total_toys >= 50:
    discount = 0.25
    total_price -= total_price * discount
total_price -= total_price * SHOP_RENT_PERCENTAGE

if total_price >= holiday_price:
    print(f"Yes! {total_price - holiday_price:.2f} lv left.")
else:
    print(f"Not enough money! {holiday_price - total_price:.2f} lv needed.")