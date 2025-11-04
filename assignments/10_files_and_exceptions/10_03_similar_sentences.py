import os
print("Looking in:", os.getcwd())
print("Files in folder:", os.listdir())


filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()

for line in contents.splitlines():
    print(line)
