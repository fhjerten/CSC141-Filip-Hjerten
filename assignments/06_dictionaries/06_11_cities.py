

cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'known as the city of light.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'has the busiest train station in the world.'
    },
    'new york': {
        'country': 'usa',
        'population': '8.5 million',
        'fact': 'home to the Statue of Liberty.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact'].capitalize()}")
