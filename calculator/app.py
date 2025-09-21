def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts the second number from the first."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides the first number by the second.
    
    Raises:
        ValueError: if the divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    """Starts the Read-Eval-Print Loop for the calculator."""
    print("Welcome to the Python CLI Calculator!")
    print("Type 'quit' at any time to quit.")
    
    while True:
        try:
            op = input("Enter operation (add, subtract, multiply, divide) or 'quit': ").strip().lower()
            if op == 'quit':
                print("Goodbye!")
                break
            
            if op not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation.")
                continue
        
            num1_str = input("Enter first number: ")
            num2_str = input("Enter second number: ")

            num1 = float(num1_str)
            num2 = float(num2_str)
            
            if op == 'add':
                result = add(num1, num2)
            elif op == 'subtract':
                result = subtract(num1, num2)
            elif op == 'multiply':
                result = multiply(num1, num2)
            elif op == 'divide':
                result = divide(num1, num2)
            
            print(f"Result: {result}")
        except ValueError as e:
            # This handles both invalid number inputs and division by zero
            print(f"Error: {e}")
        except Exception as e:
            # This is a generic fallback for any unexpected errors
            print(f"An unexpected error occurred: {e}")

    