print("Welcome to the Club", end="!\n",)
print("How old are you?", end="")
age = input()
print(f"You are {age} years old.")
if int(age) < 18:
    print("Access Denied. Too young!")
elif int(age) == 18 or int(age) <21:
    print("You can come in, but no drinking!")

else:
    print("Welcome! Enjoy your night!")