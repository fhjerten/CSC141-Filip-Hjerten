#creating a variable with whitespace

name = "\t  \n  Filip  \t\n"

# I write the name as it is

print("Original name with whitespace:")
print(name)

# I use the strip functions  

print("Using lstrip():")
print(name.lstrip())

print("Using rstrip():")
print(name.rstrip())

print("Using strip():")
print(name.strip())