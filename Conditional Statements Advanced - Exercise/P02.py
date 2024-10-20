temperature = int(input())
time = str(input())

match time:
    case "Morning":
        if temperature >= 10 and temperature <= 18:
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        elif temperature > 18 and temperature <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif temperature >= 25:
            outfit = "T-Shirt"
            shoes = "Sandals"
    case "Afternoon":
        if temperature >= 10 and temperature <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif temperature > 18 and temperature <= 24:
            outfit = "T-Shirt"
            shoes = "Sandals"
        elif temperature >= 25:
            outfit = "Swim Suit"
            shoes = "Barefoot"
    case "Evening":
        if temperature >= 10 and temperature <= 18:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif temperature > 18 and temperature <= 24:
            outfit = "Shirt"
            shoes = "Moccasins"
        elif temperature >= 25:
            outfit = "Shirt"
            shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
