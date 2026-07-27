def validate_age(age): 
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

try:
    user_age = int(input("Enter your age:"))
    validate_age(user_age)
    print("Age has been accepted.")
except ValueError as e:
    print("Error:", e)
    