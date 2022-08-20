from OOP.battery import Battery
from OOP.car import Car


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self, gas_tank):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.increment_odometer(534)
my_tesla.read_odometer()
my_tesla.fill_gas_tank(34)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


