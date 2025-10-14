# This is version 1
age = ""

while age != "quit":
    age = input("Enter your age (or 'quit' to stop): ")

    if age != "quit":
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

# This is version 2

active = True

while active:
    age = input("Enter your age (or 'quit' to stop): ")

    if age == "quit":
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

# This is version 3

while True:
    age = input("Enter your age (or 'quit' to stop): ")

    if age == "quit":
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")


