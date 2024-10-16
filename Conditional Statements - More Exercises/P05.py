from math import ceil, floor

days_count = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
tortoise_food = float(input()) / 1000

total_food = ((dog_food * days_count) +
              (cat_food * days_count) +
              (tortoise_food * days_count))

if total_food < left_food:
    print(f"{floor(left_food - total_food)} kilos of food left.")
else:
    print(f"{ceil(total_food - left_food)} more kilos of food are needed.")