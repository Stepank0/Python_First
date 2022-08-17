unconfirmedUsers = ['alice', 'mike', 'brian']
confirmedUsers = []

while unconfirmedUsers:
    currentUsers = unconfirmedUsers.pop()
    print("Verifying users " + currentUsers.title())
    confirmedUsers.append(currentUsers)

print("\nThe following users have been confirmed:")
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())

print("-------------------")

pets = ['cat', 'dog', 'frog', 'cat', 'bird', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("-------------------")

responses = {}
pollingActiv = True

while pollingActiv:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        pollingActiv = False

print("\n--- Poll Results ---")
for key, value in responses.items():
    print(key + " would like to climb " + value + ".")