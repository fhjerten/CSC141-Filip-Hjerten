
class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0  # The default value

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back!")

    def increment_login_attempts(self):
        """Increase the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


# i reate an instance and test the methods
user1 = User('filip', 'hjerten', 19, 'bethany')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# I print the number of login attempts
print(f"Login attempts: {user1.login_attempts}")

# Reset and print again to confirm it reset to 0
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
