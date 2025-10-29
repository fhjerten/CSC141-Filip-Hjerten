
class Restaurant:
  
    def __init__(self, restaurant_name, cuisine_type):
  
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # default value

    def describe_restaurant(self):
  
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
 
        print(f"{self.restaurant_name} is now open!")


# New class that comes from Restaurant
class IceCreamStand(Restaurant):
   

    def __init__(self, restaurant_name, cuisine_type):

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']

    def display_flavors(self):
  
        print("\nWe have the following ice cream flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# Create an instance of IceCreamStand
icecream_stand = IceCreamStand('Sweet Treats', 'ice cream')

# Call the method to display the flavors
icecream_stand.describe_restaurant()
icecream_stand.display_flavors()
