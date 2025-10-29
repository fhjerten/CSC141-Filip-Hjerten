# I create a lottery system.

from random import choice

# I make a list with numbers and letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Select 4 random items from the list
winning_ticket = []
for i in range(4):
    winning_ticket.append(choice(lottery_items))

# Print the winning combination
print("Any ticket matching these 4 numbers or letters wins a prize:")
print(winning_ticket)
