
person1 = {
    'first_name': 'john',
    'last_name': 'doe',
    'age': 25,
    'city': 'new york'
}

person2 = {
    'first_name': 'emma',
    'last_name': 'brown',
    'age': 30,
    'city': 'london'
}

person3 = {
    'first_name': 'liam',
    'last_name': 'smith',
    'age': 22,
    'city': 'sydney'
}

people = [person1, person2, person3]

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")
