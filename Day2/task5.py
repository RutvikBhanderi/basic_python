def calculator():
    print("Basic calculator")
    print("select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divisiopn")

    choice = input("Enter your choice (1/2/3/4):")

    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid Choice")

calculator()