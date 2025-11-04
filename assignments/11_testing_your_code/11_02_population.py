def city_country(city, country, population= ''):

    if population:
        full_name = f"{city.title()}, {country.title()} - Population {population}"
    else:
        full_name = f"{city.title()}, {country.title()}"
    return full_name

# Just a quick test of the function
print(city_country('santiago', 'chile'))
print(city_country('santiago', 'chile', 5000000))