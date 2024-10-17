day = str(input())

match day:
    case "Monday" | "Tuesday" | "Friday":
        print(12)
    case "Wednesday" | "Thursday":
        print(14)
    case "Saturday" | "Sunday":
        print(16)