
# This file stores the User class.

class User:
    def __init__(self, first_name, last_name, age, location):
        # Initialize user attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        # Print a summary of the user's information
        print(f"\nUser: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        # Print a personalized greeting
        print(f"Hello, {self.first_name.title()}! Welcome back.")
