def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):  # Changed from 'multiple' to 'multiply' for clarity
    return x * y  

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")  # Changed "Multiple" to "Divide"

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return  # Return early if input is invalid

    if choice == '1':
        result = add(num1, num2)
        print(f"The result of addition is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of subtraction is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of multiplication is: {result}")  # Corrected message
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of division is: {result}")  # Corrected message

if __name__ == "__main__":
    main()
