
# This program also reads the file learning_python.txt
import os
os.chdir(os.path.dirname(__file__))  # It makes sure Python looks in the right folder

with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

# loop through each line and replace Python with C
for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.strip())
