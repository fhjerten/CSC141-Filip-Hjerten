
# Start with the guest list from 3-6

guests = ["Nikola Tesla", "Albert Einstein", "Isaac Newton", "Marie Curie", "Elon Musk", "Ada Lovelace"]

# Inform that only two guests can come

print("Unfortunately, my new dinner table won't arrive in time, so I can only invite two people.\n")

# Remove guests until only two remain

while len(guests) > 2:
    removed_guest = guests.pop()
    print("Sorry, " + removed_guest + ", I can't invite you to dinner.")

print("\nGood news! You are still invited:")
for guest in guests:
    print("Dear " + guest + ", you are still invited to dinner at my place.")

# Remove the last two guests

del guests[0]
del guests[0]

# Show that the list is empty

print("\nFinal guest list:", guests)