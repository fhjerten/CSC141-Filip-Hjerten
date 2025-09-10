# I start by creating a friends list

friends = ["Freddie", "Jason", "Ashton"]

# This will cause an IndexError because there is no item at index 3
print(friends[3])

# Correct way:
print(friends[2])   # This works, because index 2 is the last item