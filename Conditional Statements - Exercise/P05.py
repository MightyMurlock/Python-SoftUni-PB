DECOR_PERCENTAGE_PRICE = 0.1
DISCOUNT_PERCENTAGE = 0.1

film_budget = float(input())
extras_count = int(input())
clothes_price_extra = float(input())

decor_price = film_budget * DECOR_PERCENTAGE_PRICE
extras_clothes_price = extras_count * clothes_price_extra

if extras_count > 150:
    extras_clothes_price -= extras_clothes_price * DISCOUNT_PERCENTAGE

total = decor_price + extras_clothes_price

if film_budget >= total:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total - film_budget:.2f} leva more.")