PREMIERE_TICKET_PRICE = 12
NORMAL_TICKET_PRICE = 7.5
DISCOUNT_TICKET_PRICE = 5

screening_type = str(input())
row = int(input())
column = int(input())

total = row * column

match screening_type:
    case "Premiere":
        total *= PREMIERE_TICKET_PRICE
    case "Normal":
        total *= NORMAL_TICKET_PRICE
    case "Discount":
        total *= DISCOUNT_TICKET_PRICE

print(f"{total:.2f} leva")