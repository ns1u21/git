import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiple(x, y):
    return x * y  # Corrected function name to 'multiply'

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")  # Updated text from "Multiple" to "Multiply"

    choice = input("Enter choice (1/2/3): ")

    if choice not in ['1', '2', '3']:
        print("Invalid choice! Please select 1, 2, or 3.")
        return  # Moved return statement outside to avoid skipping input section

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = multiple(num1, num2)
        print(f"The result of multiplication is: {result}")  # Corrected output message

    # The following print statement is not needed as the result is already printed in the conditionals
    # print("Result:", result)

if __name__ == "__main__":
    main()
