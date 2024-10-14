from math import pi
figure = str(input())
# area = 0

if figure == "square":
    side = float(input())
    area = side ** 2
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    radius = float(input())
    area = (radius ** 2) * pi

elif figure == "triangle":
    side_a = float(input())
    height = float(input())
    area = (height * side_a) / 2

print(f"{area:.3f}")