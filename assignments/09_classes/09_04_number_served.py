
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # default value

    def describe_restaurant(self):

        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
    
        print(f"{self.restaurant_name} is now open!")

# Create an instance called restaurant
restaurant = Restaurant('pasta palace', 'italian')

# I print the number of customers the restaurant has served
print(f"Number served: {restaurant.number_served}")

# I change this value and print again
restaurant.number_served = 25
print(f"Number served after update: {restaurant.number_served}")
