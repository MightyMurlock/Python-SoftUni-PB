#taxi
#starting price = 0.7
#day = 0.79 /km
#night = 0.9 /km

#bus
#day/night = 0.09 /km ----> km >= 20

#train
#day/night = 0.06 /km ----> km >= 100

TAXI_STARTING_PRICE = 0.7
TAXI_DAY_PRICE = 0.79
TAXI_NIGHT_PRICE = 0.9
BUS_PRICE = 0.09
BUS_KM_MIN = 20
TRAIN_PRICE = 0.06
TRAIN_KM_MIN = 100

km = int(input())
time = str(input())

if km >= BUS_KM_MIN and km < TRAIN_KM_MIN:
    price = BUS_PRICE * km
elif km >= TRAIN_KM_MIN:
    price = TRAIN_PRICE * km
else:
    if time == "day":
        price = 0.7 + (0.79 * km)
    else:
        price = 0.7 + (0.9 * km)

print(f"{price:.2f}")