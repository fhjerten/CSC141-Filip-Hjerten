def city_country(city, country):
  # I make a formatted city-country string
    formatted_city = f"{city.title()}, {country.title()}"
    return formatted_city

print(city_country('santiago', 'chile'))
print(city_country('stockholm', 'sweden'))
print(city_country('tokyo', 'japan'))
