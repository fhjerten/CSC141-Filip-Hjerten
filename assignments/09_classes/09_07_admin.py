# I creaate a user class
class User:

    def __init__(self, first_name, last_name, age, location):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):

        print(f"\nUser: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):

        print(f"Hello, {self.first_name.title()}! Welcome back.")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):
 
        self.login_attempts = 0


# Create a subclass called Admin
class Admin(User):


    def __init__(self, first_name, last_name, age, location):

        super().__init__(first_name, last_name, age, location)
        # Add a privileges attribute that stores a list
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            'can reset password'
        ]

    def show_privileges(self):

        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


# Create an instance of Admin and call the method
admin_user = Admin('filip', 'hjerten', 19, 'Albright')
admin_user.describe_user()
admin_user.show_privileges()
