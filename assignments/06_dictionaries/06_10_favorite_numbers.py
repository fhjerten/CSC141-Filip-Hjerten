

favorite_numbers = {
    'alex': [3, 7, 21],
    'emma': [5, 10],
    'liam': [2, 4, 6]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
    print()
