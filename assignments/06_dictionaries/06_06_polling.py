

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# List of people who should take the poll
people = ['jen', 'edward', 'phil', 'anna', 'mike']

# Check if each person has taken the poll
for name in people:
    if name in favorite_languages:
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take our programming poll!")
