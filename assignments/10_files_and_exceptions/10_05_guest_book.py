print("Enter 'quit' to stop adding names.")

# Keeps asking the user to add names until they type 'quit'Phi
while True:
    name = input("What is your name? ")

    if name.lower() == 'quit':
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(name + "\n")
        print(f"Welcome, {name}! Your name has been added to the guest book.")
