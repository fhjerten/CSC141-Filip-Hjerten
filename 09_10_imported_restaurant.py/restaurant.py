
# This file stores the Restaurant class.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Initialize name, cuisine type, and number served
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        # Print a summary of the restaurant
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        # Print a message that the restaurant is open
        print(f"{self.restaurant_name} is now open!")
