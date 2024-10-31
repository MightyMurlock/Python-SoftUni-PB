#хризантеми = chrysanthemums
#рози = roses
#лалета = tulips
HOLIDAY_PRICE_INCREASE = 15 / 100
TULIPS_DISCOUNT = 5 / 100
ROSES_DISCOUNT = 10 / 100
FLOWERS_DISCOUNT = 20 / 100
BOUQUET_PRICE = 2

bought_chrysanthemums = int(input())
bought_roses = int(input())
bought_tulips = int(input())
season = str(input())
holiday = str(input())

match season:
    case "Spring" | "Summer":
        chrysanthemums_price = 2
        roses_price = 4.1
        tulips_price = 2.5
    case "Autumn" | "Winter":
        chrysanthemums_price = 3.75
        roses_price = 4.50
        tulips_price = 4.15

total = ((bought_chrysanthemums * chrysanthemums_price) +
         (bought_roses * roses_price) +
         (bought_tulips * tulips_price))

if holiday == "Y":
    total += total * HOLIDAY_PRICE_INCREASE

if bought_tulips > 7 and season == "Spring":
    total -= total * TULIPS_DISCOUNT
if bought_roses >= 10 and season == "Winter":
    total -= total * ROSES_DISCOUNT
if (bought_chrysanthemums + bought_roses + bought_tulips) > 20:
    total -= total * FLOWERS_DISCOUNT

total += BOUQUET_PRICE
print(f"{total:.2f}")