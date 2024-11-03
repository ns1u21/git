def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter choice (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice! Please select 1 or 2.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
