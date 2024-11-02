TAX_FEE = 10 / 100

season = str(input()) #Spring, Summer, Autumn, Winter
km_month = float(input())

match season:
    case "Spring" | "Autumn":
        if km_month <= 5000:
            payment_per_km = 0.75

        elif km_month > 5000 and km_month <= 10000:
            payment_per_km = 0.95

        else:
            payment_per_km = 1.45
    case "Summer":
        if km_month <= 5000:
            payment_per_km = 0.90

        elif km_month > 5000 and km_month <= 10000:
            payment_per_km = 1.10

        else:
            payment_per_km = 1.45
    case "Winter":
        if km_month <= 5000:
            payment_per_km = 1.05

        elif km_month > 5000 and km_month <= 10000:
            payment_per_km = 1.25

        else:
            payment_per_km = 1.45

total = (payment_per_km * km_month) * 4
total -= total * TAX_FEE
print(f"{total:.2f}")