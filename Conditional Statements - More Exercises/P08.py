GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93
DISCOUNT_CARD_GASOLINE = 0.18
DISCOUNT_CARD_DIESEL = 0.12
DISCOUNT_CARD_GAS = 0.08
DISCOUNT_20_25 = 8 / 100
DISCOUNT_25 = 10 / 100

fuel_type = str(input())
fuel = float(input())
club_card = str(input())

if fuel_type == "Gasoline":
    if club_card == "Yes":
        total = fuel * (GASOLINE_PRICE - DISCOUNT_CARD_GASOLINE)
    else:
        total = fuel * GASOLINE_PRICE
elif fuel_type == "Diesel":
    if club_card == "Yes":
        total = fuel * (DIESEL_PRICE - DISCOUNT_CARD_DIESEL)
    else:
        total = fuel * DIESEL_PRICE
elif fuel_type == "Gas":
    if club_card == "Yes":
        total = fuel * (GAS_PRICE - DISCOUNT_CARD_GAS)
    else:
        total = fuel * GAS_PRICE

if fuel >= 20 and fuel <= 25:
    total -= total * DISCOUNT_20_25
elif fuel > 25:
    total -= total * DISCOUNT_25

print(f"{total:.2f} lv.")