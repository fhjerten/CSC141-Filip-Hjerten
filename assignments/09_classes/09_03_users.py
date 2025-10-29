# I make a User class similar to the Restaurant class from last exercise
class User:
    def __init__(self, first_name, last_name, age, location, hobby):
 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.hobby = hobby

    def describe_user(self):

        print(f"\nUser Profile:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Hobby: {self.hobby}")

    def greet_user(self):
      
        print(f"Hello, {self.first_name.title()}! Welcome back!")

# I create different users
user1 = User('filip', 'hjerten', 19, 'Albright', 'golf')
user2 = User('emma', 'smith', 22, 'New York', 'painting')
user3 = User('alex', 'johnson', 25, 'Chicago', 'gaming')

# I call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
