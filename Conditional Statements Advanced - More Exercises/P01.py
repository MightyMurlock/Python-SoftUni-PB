VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

#money for the transport == percentage of the budget and depends on the count of people
#   1 - 4 ---> 75% budget ---> transport
#   5 - 9 ---> 60% budget ---> transport
#   10 - 24 ---> 50% budget ---> transport
#   25 - 49 ---> 40% budget ---> transport
#   50 - 50> ---> 25% budget ---> transport

budget = float(input())
ticket_category = str(input())
people_count = int(input())

transport_price = 0
if people_count >= 1 and people_count <= 4:
    transport_price = budget  * 0.75
elif people_count >= 5 and people_count <= 9:
    transport_price = budget * 0.6
elif people_count >= 10 and people_count <= 24:
    transport_price = budget * 0.5
elif people_count >= 25 and people_count <= 49:
    transport_price = budget * 0.4
elif people_count >= 50:
    transport_price = budget * 0.25

money_left = budget - transport_price

match ticket_category:
    case "VIP":
        tickets_price = people_count * VIP_TICKET_PRICE

        if money_left >= tickets_price:
            print(f"Yes! You have {(money_left - tickets_price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(tickets_price - money_left):.2f} leva.")
    case "Normal":
        tickets_price = people_count * NORMAL_TICKET_PRICE
        if money_left >= tickets_price:
            print(f"Yes! You have {(money_left - tickets_price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(tickets_price - money_left):.2f} leva.")