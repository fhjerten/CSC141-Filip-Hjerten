import json

number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(number, f)

print("Your favorite number has been saved.")
