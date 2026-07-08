first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(first_number / second_number)





