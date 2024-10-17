product = str(input())
city = str(input())
quantity = float(input())

match city:
    case "Sofia":
        match product:
            case "coffee":
                price = 0.5
            case "water":
                price = 0.8
            case "beer":
                price = 1.2
            case "sweets":
                price = 1.45
            case "peanuts":
                price = 1.6
    case "Plovdiv":
        match product:
            case "coffee":
                price = 0.4
            case "water":
                price = 0.7
            case "beer":
                price = 1.15
            case "sweets":
                price = 1.30
            case "peanuts":
                price = 1.5
    case "Varna":
        match product:
            case "coffee":
                price = 0.45
            case "water":
                price = 0.7
            case "beer":
                price = 1.10
            case "sweets":
                price = 1.35
            case "peanuts":
                price = 1.55
price *= quantity
print(price)