length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percentage_empty = 1 - (float(input())) / 100

volume = (length_cm * width_cm * height_cm) / 1000
liters_needed = volume * percentage_empty
print(liters_needed)