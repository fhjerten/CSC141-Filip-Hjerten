def describe_city(city, country='Sweden'):

 # I make a sentence describing the city and country
    print(f"{city.title()} is in {country.title()}.")

describe_city('stockholm')
describe_city('gothenburg')
describe_city('reykjavik', 'iceland')
