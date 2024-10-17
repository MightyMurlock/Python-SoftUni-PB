FUEL_NORM = 25

fuel_type = str(input())
fuel = float(input())

if fuel_type == "Gasoline":
    if fuel >= FUEL_NORM:
        print("You have enough gasoline.")
    else:
        print("Fill your tank with gasoline!")
elif fuel_type == "Diesel":
    if fuel >= FUEL_NORM:
        print("You have enough diesel.")
    else:
        print("Fill your tank with diesel!")
elif fuel_type == "Gas":
    if fuel >= FUEL_NORM:
        print("You have enough gas.")
    else:
        print("Fill your tank with gas!")
else:
    print("Invalid fuel!")