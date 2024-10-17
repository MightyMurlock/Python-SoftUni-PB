product = str(input())

match product:
    case "banana" | "apple" | "kiwi" | "cherry" | "lemon" | "grapes":
        print("fruit")
    case "tomato" | "cucumber" | "pepper" | "carrot":
        print("vegetable")
    case _:
        print("unknown")