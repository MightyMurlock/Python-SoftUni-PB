budget = float(input())
season = str(input()) #Summer, Winter

if budget <= 100:
    class_type = "Economy class"

    match season:
        case "Summer":
            car_type = "Cabrio"
            price = (35 / 100) * budget
        case "Winter":
            car_type = "Jeep"
            price = (65 / 100) * budget

elif budget > 100 and budget <= 500:
    class_type = "Compact class"

    match season:
        case "Summer":
            car_type = "Cabrio"
            price = (45 / 100) * budget
        case "Winter":
            car_type = "Jeep"
            price = (80 / 100) * budget

else:
    class_type = "Luxury class"

    car_type = "Jeep"
    price = (90 / 100) * budget

print(f"{class_type}")
print(f"{car_type} - {price:.2f}")