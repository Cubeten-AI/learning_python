try:
    n1 = float(input("Enter the first number:"))
    operator = input("Enter operator(+,-,/,*,):")
    n2 = float(input("Enter the second number:"))
    if operator == "+":
        print("Result =",n1+n2)
    if operator == "-":
        print("Result =",n1-n2)
    if operator == "/":
        print("Result =",n1/n2)
    if operator == "*":
        print("Result =",n1*n2)
except ValueError:
    print("invalid input. Please enter a valid number:")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    