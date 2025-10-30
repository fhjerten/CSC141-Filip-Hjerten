# I wrote these 2 rows down below because It was looking in the wrong folder for the text file.
import os
os.chdir(os.path.dirname(__file__))

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)


with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
