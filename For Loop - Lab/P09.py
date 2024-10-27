number_count = int(input())

sum_l = 0
sum_r = 0
for l in range(number_count):
    num_l = int(input())
    sum_l += num_l

for r in range(number_count):
    num_r = int(input())
    sum_r += num_r

if sum_l == sum_r:
    print(f"Yes, sum = {sum_l}")
else:
    print(f"No, diff = {abs(sum_l - sum_r)}")