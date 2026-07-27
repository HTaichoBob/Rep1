numbers = [] 

while True:
    print("\n=== List Manager Menu ===")
    print("(a) Add a number")
    print("(b) Remove a number")
    print("(c) Display the list")
    print("(d) Quit")

    choice = input("Choose an option: ").lower()

    if choice == "a":
        try:
            value = int(input("Enter an integer to add: "))
            numbers.append(value)
            print(f"Added {value} to the list.")
        except ValueError:
            print("[ERROR]: You must enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print(f"Removed {removed} from the list.")
        except ValueError:
            print("[ERROR]: Index must be an integer.")
        except IndexError:
            print("[ERROR]: That index does not exist in the list.")

    elif choice == "c":
        print("Current List:", numbers)

    elif choice == "d":
        print("Exiting program. Goodbye.")
        break

    else:
        print("[ERROR]: Invalid menu option.")
