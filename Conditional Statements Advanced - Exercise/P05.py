budget = float(input())
season = str(input())

# if season == "summer":
#     holiday = "Camp"
# elif season == "winter":
#     holiday = "Hotel"

# if budget <= 100:
#     #Bulgaria
# elif budget > 100 and budget <= 1000:
#     #Balkan
# else:
#     #Europe

match season:
    case "summer":
        if budget <= 100:
            #Bulgaria
            holiday = "Camp"
            destination = "Bulgaria"
            expenses = budget * (30 / 100)
        elif budget > 100 and budget <= 1000:
            #Balkans
            holiday = "Camp"
            destination = "Balkans"
            expenses = budget * (40 / 100)
        else:
            #Europe
            holiday = "Hotel"
            destination = "Europe"
            expenses = budget * (90 / 100)
    case "winter":
        if budget <= 100:
            #Bulgaria
            holiday = "Hotel"
            destination = "Bulgaria"
            expenses = budget * (70 / 100)
        elif budget > 100 and budget <= 1000:
            #Balkan
            holiday = "Hotel"
            destination = "Balkans"
            expenses = budget * (80 / 100)
        else:
            #Europe
            holiday = "Hotel"
            destination = "Europe"
            expenses = budget * (90 / 100)

print(f"Somewhere in {destination}\n"
      f"{holiday} - {expenses:.2f}")