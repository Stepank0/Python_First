# 1 tack
users = ['sasha', 'alex', 'helen', 'kate', 'admin']
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again")
else:
    print("We need to find some users!")

# 2 tack
current_users = ['sasha', 'alex', 'helen', 'kate', 'mike', 'tatiana']

new_users = ['alex', 'tom', 'sara', 'olga', 'mike']

for new_user in new_users:
    if new_user in current_users:
        print("Name " + new_user.title() + " busy select another")
    else:
        print("The name " + new_user.title() + " is free.")

# 3 tack
number_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if number_lists:
    for number_list in number_lists:
        if number_list == 1:
            print(str(number_list) + "st")
        elif number_list == 2:
            print(str(number_list) + "nd")
        elif number_list == 3:
            print(str(number_list) + "rd")
        else:
            print(str(number_list) + "th")
else:
    print("Number list is empty")


