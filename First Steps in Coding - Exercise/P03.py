deposit = float(input())
deposit_term = int(input())
annual_interest_rate = float(input())

total = deposit + deposit_term * ((deposit * (annual_interest_rate / 100)) / 12)
print(total)
