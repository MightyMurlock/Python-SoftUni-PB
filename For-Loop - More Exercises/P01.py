#every even year from 1800 spends 12 000 leva.
#every odd year from 1800 spends (12 000 + (50 * his age))
#starting year 1800 at 18 years

inherited_money = float(input())
year = int(input())

spending_money = 0
starting_year = 1800
age = 18

for i in range(1800, year + 1, 1):
    if i % 2 == 0:
        spending_money += 12000
    else:
        spending_money += (12000 + (50 * age))

    age += 1

if spending_money <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {(inherited_money - spending_money):.2f} dollars left.")
else:
    print(f"He will need {(spending_money - inherited_money):.2f} dollars to survive.")

