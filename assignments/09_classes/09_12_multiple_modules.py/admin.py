# This file stores the Privileges and Admin classes.
from user import User

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
