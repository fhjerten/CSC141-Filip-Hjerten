# Original guest list
guests = ["Albert Einstein", "Leonardo da Vinci", "Elon Musk"]

# Print original invitations
print("Dear " + guests[0] + ", you are invited to dinner at my place.")
print("Dear " + guests[1] + ", you are invited to dinner at my place.")
print("Dear " + guests[2] + ", you are invited to dinner at my place.")

# One guest can't make it
print("\nUnfortunately, " + guests[1] + " can't make it to dinner.")

# Replace guest
guests[1] = "Marie Curie"

# Print new invitations
print("\nUpdated Invitations:")
print("Dear " + guests[0] + ", you are invited to dinner at my place.")
print("Dear " + guests[1] + ", you are invited to dinner at my place.")
print("Dear " + guests[2] + ", you are invited to dinner at my place.")