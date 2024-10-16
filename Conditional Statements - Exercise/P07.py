GRAPHICS_CARD_PRICE = 250
CPU_PERCENTAGE_PRICE = 35 / 100
RAM_PERCENTAGE_PRICE = 10 / 100
DISCOUNT_PERCENTAGE = 0.15

budget = float(input())
graphics_card_count = int(input())
cpu_count = int(input())
ram_count = int(input())

graphics_card_total = graphics_card_count * GRAPHICS_CARD_PRICE
cpu_total = cpu_count * (CPU_PERCENTAGE_PRICE * graphics_card_total)
ram_total = ram_count * (RAM_PERCENTAGE_PRICE * graphics_card_total)

total = graphics_card_total + cpu_total + ram_total

if graphics_card_count > cpu_count:
    total -= total * DISCOUNT_PERCENTAGE


if total <= budget:
    print(f"You have {(budget - total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total - budget):.2f} leva more!")