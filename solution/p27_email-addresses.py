import re


def email_addresses(text) -> list[str]:
    """
    Determine all the words of length 2 that start with a capital letter in a string.
    :param text: the string to consider
    :return: the list of all the email addresses
    """
    return re.findall(r"\S+@\S+\.\S+", text)


def words_len2(text) -> list[str]:
    """
    Determine all the words of length 2 that start with a capital letter in a string.
    :param text: the string to consider
    :return: the list of all the words
    """
    return re.findall("[A-Z+][A-Za-z]", text)


def read_file(filename: str) -> str:
    """
    Reads the entire text file filename into a string.
    :param filename: the name of the text file
    :return: a string corresponding to the text file
    """
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
        return ""


if __name__ == "__main__":
    textfile: str = read_file("/home/beo1/py/exercises/email-addresses.txt")
    print(f"all the words of len 2 with capital letter: {words_len2(textfile)}")
    print(f"all the {email_addresses(textfile)}")
