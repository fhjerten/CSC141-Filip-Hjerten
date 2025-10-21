def make_sandwich(*items):

# I print the sandwich items being made
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'cheese', 'lettuce')
make_sandwich('ham', 'tomato', 'mayo', 'pickles')
make_sandwich('peanut butter', 'jelly')
