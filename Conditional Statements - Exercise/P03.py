hour = int(input())
minute = int(input())

minute += 15
if minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24:
    hour -= 24

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")