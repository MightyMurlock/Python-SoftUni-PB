input1 = int(input())
input2 = int(input())
action = str(input())

match action:
    case "+":
        result = input1 + input2
        if result % 2 == 0:
            result_type = "even"
        else:
            result_type = "odd"
        print(f"{input1} {action} {input2} = {result} - {result_type}")
    case "-":
        result = input1 - input2
        if result % 2 == 0:
            result_type = "even"
        else:
            result_type = "odd"
        print(f"{input1} {action} {input2} = {result} - {result_type}")
    case "*":
        result = input1 * input2
        if result % 2 == 0:
            result_type = "even"
        else:
            result_type = "odd"
        print(f"{input1} {action} {input2} = {result} - {result_type}")
    case "/":
        if input2 == 0:
            print(f"Cannot divide {input1} by zero")
        else:
            result = input1 / input2
            print(f"{input1} {action} {input2} = {result:.2f}")
    case "%":
        if input2 == 0:
            print(f"Cannot divide {input1} by zero")
        else:
            result = input1 % input2
            print(f"{input1} {action} {input2} = {result}")