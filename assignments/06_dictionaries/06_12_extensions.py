
cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'known as the city of light',
        'famous_food': 'croissants'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'has the busiest train station in the world',
        'famous_food': 'sushi'
    },
    'new york': {
        'country': 'usa',
        'population': '8.5 million',
        'fact': 'home to the Statue of Liberty',
        'famous_food': 'pizza'
    },
    'stockholm': {
        'country': 'sweden',
        'population': '975,000',
        'fact': 'built on 14 islands connected by bridges',
        'famous_food': 'meatballs'
    }
}

print("World Cities Information:\n")

for city, info in cities.items():
    print(f"  {city.title()} ({info['country'].title()})")
    print(f"   Population: {info['population']}")
    print(f"   Fact: {info['fact'].capitalize()}.")
    print(f"   Famous Food: {info['famous_food'].title()}\n")
