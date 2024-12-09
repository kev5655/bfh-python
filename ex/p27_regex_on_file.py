import re

with open("./rsc/email-addresses.txt", "r") as f:
    word_list = []

    for line in f:
        if line == "":
            continue
        word_list += re.split(r'[ \t]', line)

    regex = re.compile("[A-Z].*")
    founds1 = []
    for word in word_list:
        if regex.match(word) and len(word) >= 2:
            founds1 += [word]

    for found in founds1:
        print(found, end=", ")
