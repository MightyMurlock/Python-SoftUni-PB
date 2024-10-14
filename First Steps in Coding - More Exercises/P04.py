EXCHANGE_RATE = 1.94

vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

total = ((vegetable_kg * vegetable_price) +
         (fruit_kg * fruit_price))
total /= EXCHANGE_RATE
print(f"{total:.2f}")