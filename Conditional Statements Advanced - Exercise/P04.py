BOAT_RENT_SPRING = 3000
BOAT_RENT_SUMMER_AUTUMN = 4200
BOAT_RENT_WINTER = 2600

#Discount on renting price
#Discount ---> <=6
DISCOUNT_1 = 10 / 100
#Discount ---> [7 - 11]
DISCOUNT_2 = 15 / 100
#Discount ---> >=12
DISCOUNT_3 = 25 / 100

#Discount ---> even
DISCOUNT_4 = 5 / 100

budget = int(input())
season = str(input())
fisher_count = int(input())

match season:
    case "Spring":
        total = BOAT_RENT_SPRING
    case "Summer":
        total = BOAT_RENT_SUMMER_AUTUMN
    case "Autumn":
        total = BOAT_RENT_SUMMER_AUTUMN
    case "Winter":
        total = BOAT_RENT_WINTER

if fisher_count <= 6:
    total -= total * DISCOUNT_1
elif fisher_count >= 7 and fisher_count <= 11:
    total -= total * DISCOUNT_2
elif fisher_count >= 12:
    total -= total * DISCOUNT_3

if fisher_count % 2 == 0 and season != "Autumn":
    total -= total * DISCOUNT_4

if budget >= total:
    print(f"Yes! You have {(budget - total):.2f} leva left.")
else:
    print(f"Not enough money! You need {(total - budget):.2f} leva.")