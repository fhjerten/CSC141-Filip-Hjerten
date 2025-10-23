# Start with same from last exercise
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open for business!")

# I make 3 different restaurant now
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
