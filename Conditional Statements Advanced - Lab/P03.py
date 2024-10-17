input = str(input())

match input:
    case "dog":
        print("mammal")
    case "crocodile" | "tortoise" | "snake":
        print("reptile")
    case _:
        print("unknown")