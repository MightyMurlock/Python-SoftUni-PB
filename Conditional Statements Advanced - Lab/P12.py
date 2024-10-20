city = str(input())
sales = float(input())

match city:
    case "Sofia":
        if sales >= 0 and sales <= 500:
            commission = 5 / 100
        elif sales > 500 and sales <= 1000:
            commission = 7 / 100
        elif sales > 1000 and sales <= 10000:
            commission = 8 / 100
        elif sales > 10000:
            commission = 12 / 100
        else:
            commission = 0
    case "Varna":
        if sales >= 0 and sales <= 500:
            commission = 4.5 / 100
        elif sales > 500 and sales <= 1000:
            commission = 7.5 / 100
        elif sales > 1000 and sales <= 10000:
            commission = 10 / 100
        elif sales > 10000:
            commission = 13 / 100
        else:
            commission = 0
    case "Plovdiv":
        if sales >= 0 and sales <= 500:
            commission = 5.5 / 100
        elif sales > 500 and sales <= 1000:
            commission = 8 / 100
        elif sales > 1000 and sales <= 10000:
            commission = 12 / 100
        elif sales > 10000:
            commission = 14.5 / 100
        else:
            commission = 0
    case _:
        commission = 0

if commission != 0:
    print(f"{commission * sales:.2f}")
else:
    print("error")