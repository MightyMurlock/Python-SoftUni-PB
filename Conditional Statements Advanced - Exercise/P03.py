ROSES_PRICE = 5
DAHLIAS_PRICE = 3.8
TULIPS_PRICE = 2.8
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.5

DISCOUNT_80_ROSES = 10 / 100
DISCOUNT_90_DAHLIAS = 15 / 100
DISCOUNT_80_TULIPS = 15 / 100

PRICE_INCREASE_120_NARCISSUS = 15 / 100
PRICE_INCREASE_80_GLADIOLUS = 20 / 100

flower_type = str(input())
flower_count = int(input())
budget = int(input())

match flower_type:
    case "Roses":
        total = flower_count * ROSES_PRICE
        if flower_count > 80:
            total -= total * DISCOUNT_80_ROSES
    case "Dahlias":
        total = flower_count * DAHLIAS_PRICE
        if flower_count > 90:
            total -= total * DISCOUNT_90_DAHLIAS
    case "Tulips":
        total = flower_count * TULIPS_PRICE
        if flower_count > 80:
            total -= total * DISCOUNT_80_TULIPS
    case "Narcissus":
        total = flower_count * NARCISSUS_PRICE
        if flower_count < 120:
            total += total * PRICE_INCREASE_120_NARCISSUS
    case "Gladiolus":
        total = flower_count * GLADIOLUS_PRICE
        if flower_count < 80:
            total += total * PRICE_INCREASE_80_GLADIOLUS

if budget >= total:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {(budget - total):.2f} leva left.")
else:
    print(f"Not enough money, you need {(total - budget):.2f} leva more.")