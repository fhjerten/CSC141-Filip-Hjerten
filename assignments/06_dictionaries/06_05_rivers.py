

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# I print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

# I print the names of all rivers
print("Rivers:")
for river in rivers:
    print(river.title())

print()

# I print the names of all countries
print("Countries:")
for country in rivers.values():
    print(country.title())
