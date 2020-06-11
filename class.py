from modules.countdown import Countdown


# creating and using a class

# class dog
class Dog:
    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
# accessing to attribute and print info
print(f"My dod's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# My dod's name is Willie.
# My dog is 6 years old.

# calling methods
my_dog.sit()
my_dog.roll_over()

# Willie is now sitting.
# Willie rolled over!

"""PRACTICING FOR CLASS"""


# restaurant
class Restaurant:
    """Initialize restaurant attribute"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing restaurant info"""
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Cuisine type: {self.cuisine_type}.")

    def open_restaurant(self):
        """Printing a message for client"""
        print(f"The {self.restaurant_name} is opened.")

    def number_serve(self):
        """Printing the number of customer the restaurant has served"""
        print(f"Customer served: {self.number_served}")

    def set_number_served(self, number):
        """Set the number of customers that have been served"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print(f"Customer served: {self.number_served}")

    def increment_number_served(self, numbers):
        """Incrementing the number of customers"""
        self.number_served += numbers


my_resto = Restaurant('Casa de Mayo', 'Mexican')

# we can first can call restaurant printing individually
print(f"Restaurant name: {my_resto.restaurant_name}.")
print(f"Cuisine type: {my_resto.cuisine_type}.")

# Restaurant name: Casa de Mayo.
# Cuisine type: Mexican.

# or we can call both method
my_resto.describe_restaurant()
# # Restaurant name: Casa de Mayo.
# # Cuisine type: Mexican.

my_resto.open_restaurant()
# The Casa de Mayo is opened.

your_resto = Restaurant("O'Charley", "American")
your_resto.describe_restaurant()
# Restaurant name: O'Charley.
# Cuisine type: American.

her_resto = Restaurant("Olive Gardern", "Italian")
her_resto.describe_restaurant()
# Restaurant name: Olive Gardern.
# Cuisine type: Italian.

restaurant = Restaurant("O'Chilli's", "American")
restaurant.describe_restaurant()
restaurant.number_serve()
# Restaurant name: O'Chilli's.
# Cuisine type: American.
# Customer served: 0

# let's see when and after setting a number of customer served
restaurant = Restaurant("O'Chilli's", "American")
restaurant.set_number_served(10)
restaurant.number_serve()
# Restaurant name: O'Chilli's.
# Cuisine type: American.
# Customer served: 10

# incrementing the customer number
restaurant.increment_number_served(2)
restaurant.number_serve()


# Customer served: 12


# a class user that takes multiple user profile info
class User:
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0

    def describe_user(self):
        """Printing user information"""
        user_details = f"{self.first_name}, {self.last_name}, \n{self.user_info} "
        return user_details

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello {self.first_name}")

    def get_login_attempts(self):
        print(f"Login attempts: {self.login_attempts} times")

    def increment_login_attempts(self):
        """Incrementing the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0"""
        self.login_attempts = 0


user_profile = User('Paul', 'Brou',
                    location='Nashville',
                    state='Tennessee')
print(user_profile.describe_user())

# Paul
# Brou
# {'location': 'Nashville', 'state': 'Tennessee'}

# testing the incrementing and reset
user_profile = User('Angela', 'Powell',
                    location='Atlanta',
                    state='Georgia')
user_profile.greet_user()
user_profile.increment_login_attempts()
user_profile.increment_login_attempts()
user_profile.get_login_attempts()
# Login attempts: 2 times
# Hello Angela

user_profile.reset_login_attempts()
user_profile.get_login_attempts()
# Login attempts: 0 times
# Hello Angela

user_profile.greet_user()


# Hello Paul

# -------Working with Classes and Instances------

def car_color(interior, exterior):
    color = f"Interior: {interior} \nExterior: {exterior}"
    return color.title()


class Car:
    def __init__(self, make, model, year, price, engine, fuel_type, vin, **options):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.engine = engine
        self.fuel_type = fuel_type
        self.vin = vin
        self.options = options
        # set a default value
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model} {self.price}" \
                    f"{self.engine} {self.fuel_type} {self.vin} {self.options} "
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    # let's modify the attribute value through a method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            """Reject the change if it attempts to roll the odometer back"""
            print("You can't roll back an odometer!")

    # let's increment an attribute's value through a method
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


new_car = Car('honda', 'accord', '2004', 21674, 'v4', 'gasoline', 'SALVR2BG1FH041029',
              MajorOptions='Leather Seats, Sunroof/Moonroof, Navigation System')
print(new_car.get_descriptive())
# 2004 Honda Accord
# 2004 Honda Accord 21674V4 Gasoline Salvr2Bg1Fh041029
# {'Majoroptions': 'Leather Seats, Sunroof/Moonroof, Navigation System'}

new_car.read_odometer()
# This car has 0 miles on it.

# we can modify the attribute value directly
new_car.odometer_reading = 50
new_car.read_odometer()
# This car has 50 miles on it.

# modify the attribute value through a method
new_car.update_odometer(50)
new_car.read_odometer()
# This car has 50 miles on it.

new_car.update_odometer(0)
# You can't roll back an odometer!

my_used_car = Car('subaru', 'outback', '2015', 24000, 'i4', 'gasoline', 'VINAHD2BG1FH04102',
                  MajorOptions='Leather Seats, Sunroof/Moonroof, Navigation System, Bluetooth, Backup Camera')
print(my_used_car.get_descriptive())

# 2015 Subaru Outback 24000I4 Gasoline Vinahd2Bg1Fh04102
# {'Majoroptions': 'Leather Seats, Sunroof/Moonroof, Navigation System, Bluetooth, Backup Camera'}

my_used_car.update_odometer(23_000)
my_used_car.read_odometer()
# This car has 23000 miles on it.

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# This car has 23100 miles on it.

new_car_color = car_color('black', 'ebony')
print(new_car_color)
# Interior Black
# Exterior: Ebony


# Inheritance

"""An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class"""

"""We can set Instances as Attributes if we feel we have a growing list of attributes and method in our class"""


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Method that reports the range of the car based on the battery size"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self, capacity=100):
        """Check the battery size and set the capacity to 100 if it isn't exist"""
        if self.battery_size == 75:
            self.battery_size = capacity
        print(f"New battery size: {self.battery_size}")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year, price, engine, fuel_type, vin, **options):
        """Initialize our attributes of the parent class."""
        super().__init__(make, model, year, price, engine, fuel_type, vin, **options)
        """Then initialize attributes specific to an electric car"""
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size."""
    #     print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', '2019', 34000, 'VLX4', 'gasoline', 'VINTTE2BG1FH04102',
                       MajorOptions='Leather Seats, Navigation System, Bluetooth, Backup Camera')
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# my_tesla.describe_battery()

# 2019 Tesla Model S 34000Vlx4 Gasoline Vintte2Bg1Fh04102
# {'Majoroptions': 'Leather Seats, Navigation System, Bluetooth, Backup Camera'}
# This car has a 75-kWh battery.
# This car can go about 260 miles on a full charge

my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

# New battery size: 100
# This car can go about 315 miles on a full charge

"""SOME INHERITANCE PRACTICING"""


class IceCreamStand(Restaurant):
    """this class inherits from the Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of restaurant class"""
        super().__init__(restaurant_name, cuisine_type)
        # storing a list of ice cream flavors
        self.flavors = ['neapolitan', 'strawberry ', 'butter pecan caramel', 'green tea', 'rocky road ']

    def display_flavors(self):
        """Displaying ice-cream"""
        flavors = f"My ice-cream flavors : {self.flavors}"
        return flavors.title()


my_icecream_flavor = IceCreamStand('Jessy Ice-Cream', 'American')
print(my_icecream_flavor.restaurant_name)
print(my_icecream_flavor.cuisine_type)
print(my_icecream_flavor.display_flavors())


# Jessy Ice-Cream
# American
# My Ice-Cream Flavors : ['Neapolitan', 'Strawberry ', 'Butter Pecan Caramel', 'Green Tea', 'Rocky Road ']


# A separate privilege class
class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        privileges = f"{self.privileges}"
        return privileges.title()


class Admin(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)

        # A list of user privileges
        self.privileges = Privileges()

    # def show_privileges(self):
    #     privileges = f"{self.privileges}"
    #     return privileges.title()


# user_profile = Admin('Paul', 'Brou',
#                     location='Nashville',
#                     state='Tennessee')
# print(user_profile.show_privileges())
# ['Can Add Post', 'Can Delete Post', 'Can Ban User']


user_profile = Admin('Paul', 'Brou',
                     location='Nashville',
                     state='Tennessee')
print(user_profile.privileges.show_privileges())
# ['Can Add Post', 'Can Delete Post', 'Can Ban User']


# c = Countdown(30)
# print(c)
