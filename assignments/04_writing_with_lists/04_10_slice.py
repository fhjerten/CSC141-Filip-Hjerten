# I create a list of the first 10 cubes using a list comprehension

cubes = [number ** 3 for number in range(1, 11)]

print("The first three items in the list are:")
print(cubes[:3])

print("\nThree items from the middle of the list are:")
print(cubes[3:6])  # Here's the middle three

print("\nThe last three items in the list are:")
print(cubes[-3:])
