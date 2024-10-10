SQ_METER_PRICE = 7.61
DISCOUNT = 0.18

sq_meters = float(input())

price = SQ_METER_PRICE * sq_meters
discounted_price = price * DISCOUNT

final_price = price - discounted_price

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discounted_price} lv.")
