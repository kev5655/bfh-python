import re


def find_words():
    with open("./rsc/email-addresses.txt", "r") as f:
        word_list = []

        for line in f:
            if line == "":
                continue
            word_list += re.split(r'[ \t]', line)

        regex = re.compile("[A-Z].*")
        founds_words = []
        for word in word_list:
            if regex.match(word) and len(word) >= 2:
                founds_words += [word]

        for found in founds_words:
            print(found, end=", ")

        founds_emails = []
        regex = re.compile(r"^\S+@\S+\.\S+$")
        for word in word_list:
            if regex.match(word):
                founds_emails += [word]

        print()

        for found in founds_emails:
            print(found, end=", ")


if __name__ == "__main__":
    find_words()
