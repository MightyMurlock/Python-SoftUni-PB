

#WD = WEEKDAY
BANANA_PRICE_WD = 2.5
APPLE_PRICE_WD = 1.2
ORANGE_PRICE_WD = 0.85
GRAPEFRUIT_PRICE_WD = 1.45
KIWI_PRICE_WD = 2.7
PINEAPPLE_PRICE_WD = 5.5
GRAPES_PRICE_WD = 3.85

#WE = WEEKEND
BANANA_PRICE_WE = 2.7
APPLE_PRICE_WE = 1.25
ORANGE_PRICE_WE = 0.9
GRAPEFRUIT_PRICE_WE = 1.60
KIWI_PRICE_WE = 3
PINEAPPLE_PRICE_WE = 5.6
GRAPES_PRICE_WE = 4.2

fruit = str(input())
day = str(input())
quantity = float(input())

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        match fruit:
            case "banana":
                price = BANANA_PRICE_WD
            case "apple":
                price = APPLE_PRICE_WD
            case "orange":
                price = ORANGE_PRICE_WD
            case "grapefruit":
                price = GRAPEFRUIT_PRICE_WD
            case "kiwi":
                price = KIWI_PRICE_WD
            case "pineapple":
                price = PINEAPPLE_PRICE_WD
            case "grapes":
                price = GRAPES_PRICE_WD
            case _:
                price = 0
    case "Saturday" | "Sunday":
        match fruit:
            case "banana":
                price = BANANA_PRICE_WE
            case "apple":
                price = APPLE_PRICE_WE
            case "orange":
                price = ORANGE_PRICE_WE
            case "grapefruit":
                price = GRAPEFRUIT_PRICE_WE
            case "kiwi":
                price = KIWI_PRICE_WE
            case "pineapple":
                price = PINEAPPLE_PRICE_WE
            case "grapes":
                price = GRAPES_PRICE_WE
            case _:
                price = 0
    case _:
        price = 0

if price != 0:
    total = price * quantity
    print(f"{total:.2f}")
else:
    print("error")