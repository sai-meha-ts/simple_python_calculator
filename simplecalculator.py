def calculator():
    print("My Simple Calculator")
    print("Select the type of operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input: please enter numeric values.")
            return

        if choice == '1':
            print("The answer is", a + b)
        elif choice == '2':
            print("The answer is", a - b)
        elif choice == '3':
            print("The answer is", a * b)
        elif choice == '4':
            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("The answer is", a / b)
    else:
        print("Invalid input: please choose 1, 2, 3, or 4.")

calculator()
