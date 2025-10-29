
#  I Simulate how many tries it takes to win the lottery.

from random import choice

# Make a list with numbers and letters
lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Your ticket to match
my_ticket = [5, 'B', 9, 'E']

# Count how many tries it takes to win
attempts = 0
winning = []

# Loop until the randomly chosen ticket matches yours
while winning != my_ticket:
    winning = []
    for i in range(4):
        winning.append(choice(lottery_items))
    attempts += 1

# Print how many attempts it took to win
print("Your ticket:", my_ticket)
print("Winning ticket:", winning)
print(f"It took {attempts} attempts to get a winning ticket!")
