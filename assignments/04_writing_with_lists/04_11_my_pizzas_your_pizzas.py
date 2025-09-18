# I start with making a list of pizzas

pizzas = ["pepperoni", "margherita", "bbq chicken"]

# I make a copy of the list

friend_pizzas = pizzas[:]

# I add a new pizza to the original list
pizzas.append("hawaiian")

# I add a different pizza to the friend's list
friend_pizzas.append("veggie")

# I prove that I have two separate lists

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
