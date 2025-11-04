import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Your favorite number has been saved.")
else:
    print(f"I know your favorite number! It's {number}.")
