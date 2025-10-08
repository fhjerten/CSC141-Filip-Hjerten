

# First I create a dictionary from the last exercise
glossary = {
    'variable': 'A named location used to store data in memory.',
    'string': 'A series of characters enclosed in quotes.',
    'loop': 'A sequence of instructions that repeats until a condition is met.',
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.'
}

# I print each term and its definition in a neatly formatted way
for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")

# I add five more terms to the glossary
glossary['function'] = 'A block of code that performs a specific task.'
glossary['tuple'] = 'An immutable list of items.'
glossary['boolean'] = 'A data type that can be either True or False.'
glossary['comment'] = 'A note in the code that Python ignores.'
glossary['module'] = 'A file containing Python code that can be imported.'

# I print the updated glossary  
print("Updated Glossary:\n")
for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")
