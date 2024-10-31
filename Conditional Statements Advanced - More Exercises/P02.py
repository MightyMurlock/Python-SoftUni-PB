CROSS_COUNTRY_DISCOUNT = 25 / 100
EXPENSES_PERCENTAGE = 5 / 100

juniors_count = int(input())
seniors_count = int(input())
track_type = str(input())

match track_type:
    case "trail":
        junior_fee = 5.50
        senior_fee = 7
    case "cross-country":
        if (juniors_count + seniors_count) >= 50:
            junior_fee = 8 - (8 * CROSS_COUNTRY_DISCOUNT)
            senior_fee = 9.50 - (9.50 * CROSS_COUNTRY_DISCOUNT)
        else:
            junior_fee = 8
            senior_fee = 9.50
    case "downhill":
        junior_fee = 12.25
        senior_fee = 13.75
    case "road":
        junior_fee = 20
        senior_fee = 21.50

money_collected = (juniors_count * junior_fee) + (seniors_count * senior_fee)
money_collected -= money_collected * EXPENSES_PERCENTAGE

print(f"{money_collected:.2f}")
