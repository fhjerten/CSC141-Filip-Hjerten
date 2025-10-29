
# This file stores the classes User, Privileges, and Admin.

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


class Privileges:
    def __init__(self):
        # Initialize privileges with a default list
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            'can reset password'
        ]

    def show_privileges(self):
        # Display the privileges
        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        # Initialize attributes of the parent class
        super().__init__(first_name, last_name, age, location)
        # Create an instance of Privileges
        self.privileges = Privileges()
