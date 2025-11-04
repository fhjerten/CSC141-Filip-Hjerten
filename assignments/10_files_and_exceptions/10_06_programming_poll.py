print("Enter two numbers and I'll add them together.")
print("Enter 'q' to quit.\n")

while True:
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        break

    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, you must enter numbers only!\n")
    else:
        print(f"The sum is: {result}\n")
