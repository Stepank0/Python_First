alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['name'] = 'stranger'
alien_0['something'] = 'thing'
print(alien_0)

print("The alien color is " + alien_0['color'] + ".")
alien_0['color'] = 'red'
print("The alien color is now " + alien_0["color"] + ".")

print("-----------------------")

alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

print("-----------------------")

del alien_0['something']
print(alien_0)

print("-----------------------")
# exercise № 1
# 1
favorit_person = {'first_name': 'kate', 'last_name': 'koryagina', 'age': 30, 'city': 'moscow'}
print("My favorit person is " + favorit_person['last_name'].title() + " " + favorit_person['first_name'].title()
      + "." + " She is from " + favorit_person['city'].title() + "." + " And she is " + str(
    favorit_person['age']) + ".")

# 2
favorit_number = {'sasha': 4, 'stephan': 42, 'kate': 18, 'mike': 7, 'helen': 77}

for name, number in favorit_number.items():
    print(str(name).title() + "'s favorit number is " + str(number))

print("-----------------------")
print("Name everyone : ")

for name in favorit_number.keys():
    print(name.title())

print("-----------------------")

my_friends = ['stephan', 'kate']

for name, number in favorit_number.items():
    print(name.title() + " hello!")

    if name in my_friends:
        print(" Hi dude! " + name.title() +
              ", I see you favorit number are " + str(number))

print("-----------------------")

for name in sorted(favorit_number.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("-----------------------")

favorit_number['fred'] = 77
for name, number in sorted(favorit_number.items()):
    print(str(name).title() + " : " + str(number))

print("All single number : ")
for number in set(favorit_number.values()):
    print(str(number))

print("-----------------------")
# exercise № 2
# 1

golosarium = {'pass': 'Оператор Python pass используется для того, чтобы ничего не делать.',
              'def': 'ключевое слово, используемое для определения функции',
              'if': 'оператор if используется для записи блока условного кода',
              'del': 'Ключевое слово del используется для удаления таких объектов, как переменные, список, объекты и т. д.',
              'return': 'Оператор return используется в функции для возврата значения',
              'and': 'Логические операторы и операции',
              'or': 'Логические операторы и операции'}

golosarium['elif'] = 'Оператор elif всегда используется вместе с оператором if для операции «else if»'

for term, value in golosarium.items():
    print(term + " : " + value)
