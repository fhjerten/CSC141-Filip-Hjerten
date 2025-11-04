filename = 'frankenstein.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} was not found.")
else:
    # Count how many times the word "the" appears in the first four chapters of Frankenstein
    word = 'the'
    count = contents.lower().count(word)
    print(f"The word '{word}' appears about {count} times in {filename}.")
