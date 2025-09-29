# equality / inequality with strings
animal = 'dog'
print("animal == 'dog'? I predict True.")
print(animal == 'dog')

print("\nanimal == 'cat'? I predict False.")
print(animal == 'cat')

# using lower()
name = 'Alice'
print("\nname.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nname.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')

# numerical tests
age = 21
print("\nage > 18? I predict True.")
print(age > 18)

print("\nage < 18? I predict False.")
print(age < 18)

# and / or
x = 5
y = 10
print("\nx < 10 and y > 5? I predict True.")
print(x < 10 and y > 5)

print("\nx > 10 or y < 5? I predict False.")
print(x > 10 or y < 5)

# in list
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)

print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# not in list
print("\nIs 'grape' not in fruits? I predict True.")
print('grape' not in fruits)

print("\nIs 'apple' not in fruits? I predict False.")
print('apple' not in fruits)
