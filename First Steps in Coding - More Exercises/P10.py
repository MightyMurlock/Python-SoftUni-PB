input = float(input())

if input >= 26 and input <= 35:
    print("Hot")
elif input >= 20.1 and input <= 25.9:
    print("Warm")
elif input >= 15 and input <= 20:
    print("Mild")
elif input >= 12 and input <= 14.9:
    print("Cool")
elif input >= 5 and input <= 11.9:
    print("Cold")
else:
    print("unknown")