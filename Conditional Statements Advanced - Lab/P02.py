input = str(input())

match input:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Working day")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Error")