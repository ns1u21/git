def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
def multiple(x,y):
    return x*y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Multiple")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select 1 or 2 or 3 or 4.")
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
        elif choice == '3':
            result = multiple(num1, num2)
            print(f"The result of subtraction is: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of subtraction is: {result}")    
   
    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
