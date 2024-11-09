import sys

max_number = -sys.maxsize
sum_numbers = 0

number_count = int(input())

for x in range(number_count):
    number = int(input())

    if number > max_number:
        max_number = number

    sum_numbers += number

sum_numbers -= max_number

if max_number == sum_numbers:
    print("Yes")
    print(f"Sum = {max_number}")

else:
    print("No")
    print(f"Diff = {abs(max_number - sum_numbers)}")