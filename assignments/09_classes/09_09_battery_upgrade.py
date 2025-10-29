
# I use the final version of electric_car.py and add an upgrade_battery() method.

class Car:
  
    def __init__(self, make, model, year):
 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
     
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
  
        print(f"This car has {self.odometer_reading} miles on it.")


class Battery:

    def __init__(self, battery_size=40):
   
        self.battery_size = battery_size

    def describe_battery(self):
  
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
  
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
 
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh!")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance of Battery


# Make an electric car with a default battery size
my_tesla = ElectricCar('tesla', 'model 3', 2025)

# Show range before upgrade
my_tesla.battery.get_range()

# Upgrade the battery
my_tesla.battery.upgrade_battery()

# Show range after upgrade
my_tesla.battery.get_range()
