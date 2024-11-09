p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

number_count = int(input())

for x in range(number_count):
    number = int(input())

    if number < 200:
        p1_count += 1
    elif 200 <= number <= 399:
        p2_count += 1
    elif 400 <= number <= 599:
        p3_count += 1
    elif 600 <= number <= 799:
        p4_count += 1
    elif number >= 800:
        p5_count += 1

p1 = f"{((p1_count / number_count) * 100):.2f}%"
p2 = f"{((p2_count / number_count) * 100):.2f}%"
p3 = f"{((p3_count / number_count) * 100):.2f}%"
p4 = f"{((p4_count / number_count) * 100):.2f}%"
p5 = f"{((p5_count / number_count) * 100):.2f}%"

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
