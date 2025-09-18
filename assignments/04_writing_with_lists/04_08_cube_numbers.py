# I Make a list of the first 10 cubes

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# I print each cube
for cube in cubes:
    print(cube)
