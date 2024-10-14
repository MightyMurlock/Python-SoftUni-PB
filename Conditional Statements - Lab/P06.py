input = float(input())

if input <= 10:
    print("slow")
elif input > 10 and input <= 50:
    print("average")
elif input > 50 and input <= 150:
    print("fast")
elif input > 150 and input <= 1000:
    print("ultra fast")
else:
    print("extremely fast")