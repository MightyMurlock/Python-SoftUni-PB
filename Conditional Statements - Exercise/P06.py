from math import floor

DELAY_TIME = 12.5
DELAY_DISTANCE = 15

record_time = float(input())
distance = float(input())
time_one_meter = float(input())

competing_time = distance * time_one_meter
competing_time += (distance // DELAY_DISTANCE) * DELAY_TIME
# delay_time = floor((distance / DELAY_DISTANCE) * DELAY_TIME)
# delay_time = (distance / DELAY_DISTANCE) * DELAY_TIME
# competing_record = floor(competing_time + delay_time)

if competing_time < record_time:
    print(f"Yes, he succeeded! The new world record is {competing_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(competing_time - record_time):.2f} seconds slower.")