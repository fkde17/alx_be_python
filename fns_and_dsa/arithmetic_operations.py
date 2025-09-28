num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()


def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            print(f"Result: {num1 + num2}")
        case "subtract":
            print(f"Result: {num1 - num2}")
        case "multiply":
            print(f"Result: {num1 * num2}")
        case "division":
            if num2 == 0:
                print("Error: DIVISION BY ZERO")
            else:
                print(f"Result: {num1 / num2}")

perform_operation(num1,num2,operation)


