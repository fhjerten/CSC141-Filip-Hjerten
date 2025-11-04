filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass   # Makes it fail silently with no error message if the file is not found
    else:
        print(f"\nContents of {filename}:")
        print(contents)
