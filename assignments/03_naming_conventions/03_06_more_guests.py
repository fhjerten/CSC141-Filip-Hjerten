# The guest list after 3-5

guests = ["Albert Einstein", "Marie Curie", "Isaac Newton"]

# I let everyone know that I found a bigger table

print ("Good news! I found a bigger dinner table, so more guests are invited.")

# I add one more guest

guests.insert(0, "Jeff Bezos")

# Add one more

guests.insert(2,"Bill Gates")

# Add one more

guests.append("Ada Lovelace")

# Print new invitations

for guest in guests:
    print("Dear " + guest + ", you are invited to dinner at my place.")
    
