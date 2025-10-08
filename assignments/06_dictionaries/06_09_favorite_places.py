
favorite_places = {
    'alex': ['paris', 'tokyo', 'new york'],
    'emma': ['london', 'rome'],
    'liam': ['sydney']
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")
    print()
