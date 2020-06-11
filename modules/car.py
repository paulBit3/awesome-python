# A module

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
