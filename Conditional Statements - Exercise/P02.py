input = int(input())
bonus = 0

if input <= 100:
    bonus += 5
elif input > 100 and input <= 1000:
    bonus += input * 0.2
else:
    bonus += input * 0.1

if input % 2 == 0:
    bonus += 1
elif input % 5 == 0:
    bonus += 2

print(bonus)
print(input + bonus)