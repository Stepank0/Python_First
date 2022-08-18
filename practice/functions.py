def first():
    """Вывод информации"""
    print('Hello!')


first()


def greet_user(user_Name):
    """Выводит простое приветствие."""
    for name in user_Name:
        msg = "Hello, " + name.title() + "!"
        print(msg)


greet_user("mike")


def describe_pet(pet_name, animal_type='dog'):
    """Выводит информацию о животном."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


def get_formatted_name(fist_name, second_name, middle_name=''):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = fist_name + ' ' + middle_name + ' ' + second_name
    else:
        full_name = fist_name + " " + second_name
    return str(full_name.title())


musician = get_formatted_name('mike', 'smith', 'lee')
print(musician)


def build_person(first_name, second_name, age=''):
    """Возвращает словарь с информацией о человеке."""
    full_info = {'first': first_name, 'second': second_name}

    if age:
        full_info['age'] = age
    return full_info


person = build_person('lee', 'hendrix', 27)

print(person)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q' or f_name == 'Q':
        break

    s_name = input("Second name: ")
    if s_name == 'q' or s_name == 'Q':
        break

    m_name = input("Middle name: ")
    if m_name == 'q' or m_name == 'Q':
        break

    formatted_name = get_formatted_name(f_name, s_name, m_name)
    print(formatted_name)

usernames = ['lee', 'mike', 'sara', 'don']
greet_user(usernames)


def print_models(unprinted_designs, compleat_designs):
    """Имитирует печать моделей, пока список не станет пустым.
     Каждая модель после печати перемещается в completed_models."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Имитация печати модели на 3D-принтере.
        print("Printing model: " + current_design)
        compleat_designs.append(current_design)


def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def make_pizza(size, *toppings):
    """Выводит описание пиццы."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print(" - " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(f_name, s_name, **user_info):
    profile = {}
    profile['first_name'] = f_name
    profile['second_name'] = s_name
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
