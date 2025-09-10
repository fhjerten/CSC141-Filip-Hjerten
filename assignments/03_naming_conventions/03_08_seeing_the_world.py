# List of places I'd like to visit (not in alphabetical order)

places = ["Tokyo", "Paris", "New York", "Sydney", "Rome"]

# Original list

print("Original list:", places)

# Alphabetical order (without changing the list)

print("Alphabetical order:", sorted(places))

# Show original list again

print("Still original:", places)

# Reverse-alphabetical order (without changing the list)

print("Reverse alphabetical order:", sorted(places, reverse=True))

# Show original list again

print("Still original:", places)

# I Reverse the order of the list

places.reverse()
print("Reversed order:", places)

# I Reverse it again to get back to original

places.reverse()
print("Back to original order:", places)

# Sort the list alphabetically 

places.sort()
print("Sorted alphabetically:", places)

# Sort the list in reverse alphabetical order

places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)