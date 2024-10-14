NYLON_PRICE = 1.5
PAINT_PRICE = 14.5
PAINT_THINNER_PRICE = 5
BAGS_PRICE = 0.4
WORKERS_TAX = 0.3

nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())

total = (((nylon + 2) * NYLON_PRICE) +
         ((paint + (paint * 0.1)) * PAINT_PRICE) +
         (paint_thinner * PAINT_THINNER_PRICE) +
         BAGS_PRICE)
worker_payment = (total * WORKERS_TAX) * hours
total += worker_payment
print(total)