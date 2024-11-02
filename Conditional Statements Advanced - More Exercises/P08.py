# {x, y} - point
# rectangle
# {x1, y1} - point of rectangle
# {x2, y2} - point of rectangle

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

on_top_side = False
on_bottom_side = False
on_right_side = False
on_left_side = False

#top side {x1, y1}
if x >= x1 and x <= x2 and y == y1:
    on_top_side = True

#bottom side {x2, y2}
if x >= x1 and x <= x2 and y == y2:
    on_bottom_side = True

#right side
if y >= y1 and y <= y2 and x == x2:
    on_right_side = True

#left side
if y >= y1 and y <= y2 and x == x1:
    on_left_side = True

if on_top_side or on_bottom_side or on_right_side or on_left_side:
    print("Border")
else:
    print("Inside / Outside")