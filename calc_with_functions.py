def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operation. Use +, -, *, or /."

def main():
    print("Simple Calculator (with functions)")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    op = input("Enter operation (+, -, *, /): ")

    result = calculate(a, b, op)
    print("Result:", result)

if __name__ == "__main__":
    main()
