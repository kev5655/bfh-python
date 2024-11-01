def nb_words_string(line: str):
    """
    Determine the number of words in a string. A word starts with a letter (lower or uppercase letter)
    followed by zero of more letters (lowercase or uppercase) or digits.
    :param line: input string
    :return the number of words in the string
    """
    i = 0
    nb_words = 0
    while i < len(line):
        while i < len(line) and (not line[i].isalpha()):  # skip non letters after a word
            i += 1
        if i < len(line) and line[i].isalpha():  # a word starts with a letter
            nb_words += 1
            i += 1
            while i < len(line) and line[i].isalnum():  # skip letters or digits that compose a word
                i += 1
    return nb_words


def nb_words_file(filename: str) -> int:
    """
    Reads the text file filename line by line and determine the number of words
    contained in the text file.  A word starts with a letter (lower or uppercase letter)
    followed by zero of more letters (lowercase or uppercase) or digits.
    :param filename: the name of the text file
    :return: the number of words contained in the text file
    """
    total_nb_words = 0
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            for line in file:
                line_wo_newlines = line[:-1]
                total_nb_words += nb_words_string(line_wo_newlines)  # ignore the newline
            return total_nb_words
    except FileNotFoundError:
        print(f"File {filename} does not exist.")


if __name__ == "__main__":
    result = nb_words_file("/home/beo1/py/exercises/email-addresses.txt")
    print(result)
