class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется."""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
            """Увеличивает показания одометра с заданным приращением."""
            self.odometer_reading += miles

    def fill_gas_tank(self, gas_tank):
        print("refuel with gasoline for " + str(gas_tank) + " liters")


my_car = Car('audi', 'a6', 2019)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.update_odometer(23)
my_car.read_odometer()
my_car.update_odometer(3)
my_car.increment_odometer(100)
my_car.read_odometer()
my_car.fill_gas_tank(40)

