hour = int(input())
day = str(input())

if day != "Sunday":
    if hour >= 10 and hour <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")