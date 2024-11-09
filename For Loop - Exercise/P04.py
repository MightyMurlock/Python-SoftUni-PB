savings = 0
toy_count = 0

lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

for x in range(1, lily_age + 1):
    if x % 2 == 0:
        savings += (5 * x) - 1
    else:
        savings += toy_price

if savings >= washing_machine_price:
    print(f"Yes! {(savings - washing_machine_price):.2f}")
else:
    print(f"No! {(washing_machine_price - savings):.2f}")