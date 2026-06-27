def calculator():
    print("=== Simple Python Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:  # Loop until user exits
        # Get first number
        num1_input = input("Enter first number: ")
        if num1_input.lower() == "exit":
            print("Goodbye!")
            break

        # Get second number
        num2_input = input("Enter second number: ")
        if num2_input.lower() == "exit":
            print("Goodbye!")
            break

        # Get operation
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation.lower() == "exit":
            print("Goodbye!")
            break

        try:
            # Convert inputs to float (data type conversion)
            num1 = float(num1_input)
            num2 = float(num2_input)

            # Conditional checks for operation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                print("Invalid operation. Please use +, -, *, or /.")
                continue  # Skip to next loop iteration

            # Output result
            print(f"Result: {result}\n")

        except ValueError:
            print("Error: Please enter valid numbers.\n")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}\n")
        except Exception as e:
            print(f"Unexpected error: {e}\n")

# Run the calculator
calculator()
