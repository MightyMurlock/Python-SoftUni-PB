DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4

dog_food_count = int(input())
cat_food_count = int(input())

dog_food_total = DOG_FOOD_PRICE * dog_food_count
cat_food_total = CAT_FOOD_PRICE * cat_food_count
total_price = dog_food_total + cat_food_total

print(f"{total_price} lv.")
