def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("Welcome to the Robust Calculator!")
    while True:
        print("\nSelect operation: +, -, *, / or 'q' to quit")
        choice = input("Enter choice: ").strip()

        if choice.lower() == 'q':
            print("Goodbye!")
            break

        if choice not in ('+', '-', '*', '/'):
            print("Invalid choice, try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
