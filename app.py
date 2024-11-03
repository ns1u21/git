import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    if len(sys.argv) != 4:
        print("Usage: app.py <operation> <num1> <num2>")
        print("Operation should be 'add' or 'subtract'")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    else:
        print("Invalid operation. Use 'add' or 'subtract'.")
        sys.exit(1)

    print("Result:", result)

if __name__ == "__main__":
    main()
