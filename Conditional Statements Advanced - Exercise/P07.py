DISCOUNT_STUDIO_1 = 5 / 100
DISCOUNT_STUDIO_2 = 30 / 100
DISCOUNT_STUDIO_3 = 20 / 100
DISCOUNT_APARTMENT = 10 / 100

month = str(input())
nights = int(input())

match month:
    case "May" | "October":
        price_studio_night = 50
        price_apartment_night = 65
        if nights > 14:
            price_studio_night -= price_studio_night * DISCOUNT_STUDIO_2
            price_apartment_night -= price_apartment_night * DISCOUNT_APARTMENT
        elif nights > 7:
            price_studio_night -= price_studio_night * DISCOUNT_STUDIO_1
    case "June" | "September":
        price_studio_night = 75.20
        price_apartment_night = 68.70
        if nights > 14:
            price_studio_night -= price_studio_night * DISCOUNT_STUDIO_3
            price_apartment_night -= price_apartment_night * DISCOUNT_APARTMENT
    case "July" | "August":
        price_studio_night = 76
        price_apartment_night = 77
        if nights > 14:
            price_apartment_night -= price_apartment_night * DISCOUNT_APARTMENT

price_studio = price_studio_night * nights
price_apartment = price_apartment_night * nights

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")