class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.__make = make
        self.__model = model
        self.__year = year
        self.odometer_reading = 0

    def __check_value(year):
        if (isinstance(year, int)):
            return True
        else:
            return False

    def get_info(self):
        return self.__make, self.__model, self.__year

    def set_About_Car(self, make, model, year):
        if(Car.__check_value(year)):
            self.__model = model
            self.__make = make
            self.__year = year
        else:
            print("Год введен не числом")

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.__year) + ' ' + self.__make + ' ' + self.__model
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

print(my_car.get_info())

my_car.set_About_Car('mazda', 'cx-5', '2015')
print(my_car.get_info())
