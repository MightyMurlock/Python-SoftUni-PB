from math import ceil, floor

#vineyard with area X - 40% of harvest ---> production of wine
#1 m^2 of area X ---> Y grapes kg
#1 liter wine == 2.5 kg grapes
#Z liters == wanted wine liters
#if production of wine == Z liters ---> ((prod. wine) - Z liters) / workers
WINE_PRODUCTION_PERCENTAGE = 0.4
GRAPES_WINE_LITER = 2.5

vineyard_area = int(input())
grapes_kg_sqM = float(input())
wanted_wine = int(input())
workers_count = int(input())

grapes_production = vineyard_area * grapes_kg_sqM
wine_production = (grapes_production * WINE_PRODUCTION_PERCENTAGE) / GRAPES_WINE_LITER

if wine_production < wanted_wine:
    print(f"It will be a tough winter! More {floor(wanted_wine - wine_production)} liters wine needed.")
else:
    liters_left = ceil(wine_production - wanted_wine)
    wine_person = ceil(liters_left / workers_count)
    print(f"Good harvest this year! Total wine: {floor(wine_production)} liters.")
    print(f"{liters_left} liters left -> {wine_person} liters per person.")