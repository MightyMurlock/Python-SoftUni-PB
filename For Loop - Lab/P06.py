input_text = str(input())

sum = 0
for char in input_text:
    match char:
        case "a":
            sum += 1
        case "e":
            sum += 2
        case "i":
            sum += 3
        case "o":
            sum += 4
        case "u":
            sum += 5

print(sum)