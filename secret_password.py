secret = "python123"
counter = 0
max_attempts = 3

while counter < max_attempts:
    user_input = input("Enter the password: ")
    
    if user_input == secret:
        print("Access granted!")
        break
    else:
        counter += 1
        print(f"Incorrect password. You have {max_attempts - counter} attempts left.")

if counter == max_attempts:
    print("Access denied. Too many failed attempts.")





