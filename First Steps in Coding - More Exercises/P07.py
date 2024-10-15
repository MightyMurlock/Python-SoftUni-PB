#green paint = 1 liter for 3.4m^2
#red paint = 1 liter for 4.3m^2

#walls
#front and back walls - squares with side x
#   front wall has a door - 1.2 m * 2 m
#side walls = rectangles with sides x and y
#   both walls have a square window - 1.5 m

#roof
#two rectangles with sides x and y
#two equilateral triangles with side x and height h

GREEN_PAINT_LITER = 3.4
RED_PAINT_LITER = 4.3
DOOR_AREA = 1.2 * 2
WINDOW_AREA = 1.5 ** 2

x = float(input())
y = float(input())
h = float(input())

#walls
#front and back walls
walls = ((2 * (x ** 2)) + (2 * (x * y))) - DOOR_AREA - (2 * WINDOW_AREA)
roof = (2 * ((x * h) / 2)) + (2 * (x * y))

green_paint = walls / GREEN_PAINT_LITER
red_paint = roof / RED_PAINT_LITER

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")