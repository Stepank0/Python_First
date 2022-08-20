class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.__name = name
        self.__age = age

    def set_name(self, name):
        if(isinstance(name, str)):
            self.__name = name
        else:
            print("Имя введено не правильно")

    def set_age(self, age):
        if(isinstance(age, int) or isinstance(age, float)):
            self.__age = age
        else:
            print("Возраст не введен правильно")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def sit(self):
        """Собака садится по команде."""
        print(self.get_name().title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.get_name().title() + " rolled over!")


my_dog = Dog('Willie', 6)
print("My dog's name is " + my_dog.get_name().title() + ".")
print("My dog is " + str(my_dog.get_age()) + " years old.")
my_dog.sit()
my_dog.roll_over()


your_dog = Dog('lusi', 3)
print("\nYour dog's name is " + your_dog.get_name().title() + ".")
print("Your dog is " + str(your_dog.get_age()) + " years old.")
your_dog.sit()

your_dog.name = "helen"

print(your_dog.name)