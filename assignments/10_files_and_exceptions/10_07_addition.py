print("Enter two numbers and I'll add them together.")
print("Type 'q' to quit.\n")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Enter the second number: ")
    if second_number.lower() == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("You can only enter numbers!\n")
    else:
        print("The sum is:", result, "\n")
