# I create a glossary of programming terms
glossary = {
    "variable": "A name used to store data that can be changed during program execution.",
    "list": "A collection of items that can be modified.",
    "tuple": "A collection of items that cannot be modified.",
    "dictionary": "A collection of key-value pairs used to store related information.",
    "loop": "A structure for repeating a set of instructions until a condition is met."
}

# Printing formatted output
for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")
