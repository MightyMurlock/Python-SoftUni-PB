CHICKEN_MENU = 10.35
FISH_MENU = 12.4
VEGETARIAN_MENU = 8.15
DELIVERY = 2.5
DESERT_PERCENTAGE = 0.2

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

total = ((chicken_menu_count * CHICKEN_MENU) +
         (fish_menu_count * FISH_MENU) +
         (vegetarian_menu_count * VEGETARIAN_MENU))
desert_price = total * DESERT_PERCENTAGE
total += desert_price + DELIVERY
print(total)

