# i make a die class

from random import randint

class Die:
    def __init__(self, sides=6):
        # I initialize the die with a default of 6 sides
        self.sides = sides

    def roll_die(self):
        # Print a random number between 1 and the number of sides
        print(randint(1, self.sides))


# Make a 6-sided die and roll it 10 times
print("6-sided die rolls:")
six_sided = Die()
for i in range(10):
    six_sided.roll_die()

# Make a 10-sided die and roll it 10 times
print("\n10-sided die rolls:")
ten_sided = Die(10)
for i in range(10):
    ten_sided.roll_die()

# Make a 20-sided die and roll it 10 times
print("\n20-sided die rolls:")
twenty_sided = Die(20)
for i in range(10):
    twenty_sided.roll_die()
