filepath_pi = "../text_file/pi_digits.txt"
filepath_pi_million = "../text_file/pi_4million_digits.txt"
filename_write = '../text_file/programming.txt'
filename_not_found = '../text_file/alice.txt'

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

# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_million:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

with open(filename_write, "w") as w_object:
    w_object.write("I love programming\n")
    w_object.write("I love creating new games.\n")

with open(filename_write, 'a') as a_object:
    a_object.write("I also love finding meaning in large datasets.\n")
    a_object.write("I love creating apps that can run in a browser.\n")

try:
    with open(filename_not_found) as read_object:
        book = read_object.read()
        print(book)
except FileNotFoundError:
    msg = "Sorry, the file " + filename_not_found + " does not exist."
    print(msg.rstrip())
else:
    words = book.split()
    num_words = len(words)
    print("The file " + filename_not_found + " has about " + str(num_words) +
          " words.")

