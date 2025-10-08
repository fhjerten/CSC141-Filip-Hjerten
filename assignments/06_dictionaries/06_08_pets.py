
pet1 = {
    'animal': 'dog',
    'owner': 'alex'
}

pet2 = {
    'animal': 'cat',
    'owner': 'sarah'
}

pet3 = {
    'animal': 'parrot',
    'owner': 'mike'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}\n")
