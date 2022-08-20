def count_words(path_name):
    """Подсчет приблизительного количества строк в файле."""

    try:
        with open(path_name) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + path_name + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + path_name + " has about " + str(num_words) +
              " words.")


just_file = '../text_file/alice.txt'
book_1 = '../text_file/pi.txt'
book_2 = '../text_file/pi_4million_digits.txt'
book_3 = '../text_file/pi_digits.txt'
count_words(just_file)

filenames = [just_file, book_3, book_2, book_1]
for filename in filenames:
    count_words(filename)


