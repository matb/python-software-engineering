class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, kilemeters):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = kilemeters
        else:            print("You can't roll back an odometer!")
        
    def increment_odometer(self, kilemeters):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += kilemeters

        
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model,year)
        self.battery = 0
    
    def fill(self, amount: Electricity):
        self.batter += amount
    
    
class HydrogenCar(Car):
    """Represent aspects of a car, specific to hydrogen vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model,year)
        self.hydrogen_tank = 0
    
    def fill(self, amount: Hydrogen):
        self.hydrogen_tank += amount
    
class DieselCar(Car):
    """Represent aspects of a car, specific to diesel vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model,year)
        self.diesel_tank = 0
        
    def fill(self, amount: Diesel):
        self.diesel_tank += amount