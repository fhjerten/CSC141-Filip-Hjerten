
# Write a separate Privileges class and use it in the Admin class.

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


class Privileges:
   
    def __init__(self):
     
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


class Admin(User):

    def __init__(self, first_name, last_name, age, location):

        super().__init__(first_name, last_name, age, location)
        # Make a Privileges instance as an attribute
        self.privileges = Privileges()


# Create an Admin instance and show privileges
admin_user = Admin('filip', 'hjerten', 19, 'bethany')
admin_user.describe_user()
admin_user.privileges.show_privileges()
