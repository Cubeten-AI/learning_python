choice=input("Enter\n 1 for addition,\n 2 for subtraction,\n 3 for multiplication,\n 4 for division,\n 5 for modulus,\n or anything else to exit:\n")

while True:

    match choice:

        case "1" | "2" | "3" | "4" | "5":

            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            except:
                print("Error: Please enter valid numbers.")
                exit()

            if choice == "1":
                print("Result:", x + y)
            elif choice == "2":
                print("Result:", x - y)
            elif choice == "3":
                print("Result:", x * y)
            elif choice == "4":
                if y != 0:
                    print("Result:", x / y)
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == "5":
                if y != 0:
                    print("Result:", x % y)
                else:
                    print("Error: Modulus by zero is not allowed.")
        case _:
            print("Exiting the calculator program!")
            break

    user_choice = input("Do you want to perform another calculation? (yes/no): ")

    if user_choice == "no":
        print("Exiting the calculator program!")
        break
    
    choice = input("Enter\n 1 for addition,\n 2 for subtraction,\n 3 for multiplication,\n 4 for division,\n 5 for modulus,\n or anything else to exit:\n")