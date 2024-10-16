v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_total = p1 * h
p2_total = p2 * h
total_pipe_water_volume = p1_total + p2_total
p1_percentage = f"{p1_total / total_pipe_water_volume * 100:.2f}"
p2_percentage = f"{p2_total / total_pipe_water_volume * 100:.2f}"

if total_pipe_water_volume <= v:
    total_pipe_water_percentage = f"{(total_pipe_water_volume / v) * 100:.2f}"
    print(f"The pool is {total_pipe_water_percentage}% full. Pipe 1: {p1_percentage}%. Pipe 2: {p2_percentage}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {(total_pipe_water_volume - v):.2f} liters.")
