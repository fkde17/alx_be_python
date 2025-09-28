num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()


def perform_operation(num1, num2, operation):

    match operation:
        case "add":
             return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "division":
            if num2 == 0:
                return "Error: DIVISION BY ZERO"
            elif num2!= 0:
                return num1 / num2

result = perform_operation(num1,num2,operation)
print(result)



