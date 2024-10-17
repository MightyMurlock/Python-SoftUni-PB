age = float(input())
gender = str(input())

match gender:
    case "m":
        if age >= 16:
            title = "Mr."
        else:
            title = "Master"
    case "f":
        if age >= 16:
            title = "Ms."
        else:
            title = "Miss"
print(title)