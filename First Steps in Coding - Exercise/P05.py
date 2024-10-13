PEN_PRICE = 5.8
MARKER_PRICE = 7.2
CLEANER_PRICE = 1.2

pen_count = int(input())
marker = int(input())
cleaner_liter = int(input())
discount_percent = int(input()) / 100

total = (pen_count * PEN_PRICE) + (marker * MARKER_PRICE) + (cleaner_liter * CLEANER_PRICE)
total -= (total * discount_percent)
print(total)
