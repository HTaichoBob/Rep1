# exception_demo.py

def safe_divide(a, b):
    """Return a / b unless b is zero, in which case raise ValueError."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

print("Testing safe_divide...")

test_values = [(10, 2), (5, 0), (9, 3)]

for a, b in test_values:
    try:
        result = safe_divide(a, b)
        print(f"{a} / {b} = {result}")
    except ValueError as e:
        print(f"Error during division: {e}")
    finally:
        print("Division operation completed\n")


print("Testing generic exception handling...")

try:
    number = int("not_a_number") 
    print("Converted number:", number)
except Exception as e:
    print(f"Generic exception caught: {e}")
