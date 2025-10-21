def favorite_book(title):

# I write a message about someone's favorite book
    print(f"One of my favorite books is {title}.")


def make_shirt(size='large', message='I love Python'):

# I summarize the shirt that is going to be made
    print(
        f"I'm going to make a {size}-sized shirt "
        f"with the message '{message}' printed on it."
    )


def city_country(city, country):

# I return a formatted city-country string
    return f"{city.title()}, {country.title()}"


# Example calls
favorite_book('Alice in Wonderland')
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Code. Sleep. Repeat.')
print(city_country('stockholm', 'sweden'))
