annual_fee = int(input())

shoes = annual_fee - (annual_fee * 0.4)
clothes = shoes - (shoes * 0.2)
ball = 0.25 * clothes
accesories = 0.2 * ball

total = (annual_fee +
         shoes +
         clothes +
         ball +
         accesories)
print(total)
