#per night
ONE_PERSON_ROOM = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35
#discounts
DISCOUNT_10 = 10 / 100
DISCOUNT_15 = 15 / 100
DISCOUNT_20 = 20 / 100
DISCOUNT_30 = 30 / 100
DISCOUNT_35 = 35 / 100
DISCOUNT_50 = 50 / 100

POSITIVE_RATING_INCREASE = 25 / 100
NEGATIVE_RATING_DISCOUNT = 10 / 100

days = int(input())
type_accommodation = str(input())
rating = str(input())

nights = days - 1

if days < 10:
    match type_accommodation:
        case "room for one person":
            total = nights * ONE_PERSON_ROOM
        case "apartment":
            total = nights * APARTMENT
            total -= total * DISCOUNT_30
        case "president apartment":
            total = nights * PRESIDENT_APARTMENT
            total -= total * DISCOUNT_10
elif days >= 10 and days <= 15:
    match type_accommodation:
        case "room for one person":
            total = nights * ONE_PERSON_ROOM
        case "apartment":
            total = nights * APARTMENT
            total -= total * DISCOUNT_35
        case "president apartment":
            total = nights * PRESIDENT_APARTMENT
            total -= total * DISCOUNT_15
elif days > 15:
    match type_accommodation:
        case "room for one person":
            total = nights * ONE_PERSON_ROOM
        case "apartment":
            total = nights * APARTMENT
            total -= total * DISCOUNT_50
        case "president apartment":
            total = nights * PRESIDENT_APARTMENT
            total -= total * DISCOUNT_20

match rating:
    case "positive":
        total += total * POSITIVE_RATING_INCREASE
    case "negative":
        total -= total * NEGATIVE_RATING_DISCOUNT

print(f"{total:.2f}")