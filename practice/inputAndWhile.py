prompt = "Input something : "
message = ''
active = True

while active:
    message = input(prompt)

    if message == "exit" or message == "Exit":
        active = False
        print(message)
    else:
        print(message)

a = [ x**2 for x in range(1,11)]
print(a)


alien = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    alien.append(new_alien)

for aliens in alien[:5]:
    print(aliens)
print("----")