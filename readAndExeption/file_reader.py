filepath_pi = "../pi_digits.txt"
filepath_pi_million = "../pi_4million_digits.txt"
filename_write = '../programming.txt'

with open(filepath_pi) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filepath_pi) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filepath_pi) as file_object:
    lines = file_object.readlines()
    pi_string = ""
    for line in lines:
        pi_string += line.rstrip()

print(lines)
print(pi_string)
print(len(pi_string))

with open(filepath_pi_million) as file_object:
    all_lines = file_object.readlines()

    pi_million = ""
    for line in all_lines:
        pi_million += line.rstrip()

print(len(pi_million))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_million:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

with open(filename_write, "w") as w_object:
    w_object.write("I love programming\n")
    w_object.write("I love creating new games.\n")

with open(filename_write, 'a') as a_object:
    a_object.write("I also love finding meaning in large datasets.\n")
    a_object.write("I love creating apps that can run in a browser.\n")
