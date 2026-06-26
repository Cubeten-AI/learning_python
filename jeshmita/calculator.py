while True:
    op = input("\nEnter operator (+, -, *, /) or q to quit: ")

    if op == "q":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result =", num1 + num2)
    elif op == "-":
        print("Result =", num1 - num2)
    elif op == "*":
        print("Result =", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")