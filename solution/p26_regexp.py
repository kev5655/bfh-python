import re


def vowel(s: str):
    """
    Determine if a string contains a vowelReturn True if the string contains a vowel.
    :param s: the string to check
    :return: return the match of the first occurrence, none otherwise
    """
    return re.search("[aeiouy]+", s)


def num_int(s: str):
    """
    Determine if a string denotes an integer, i.e. a digit >= 1 followed by zero or more digits or 0
    '^' and '$' ensure that it starts and ends with a digit.
    :param s: the string
    :return: return the match, none otherwise
    """
    return re.search("^0|([1-9]\d*)$", s)


def valid_date(s: str):
    """
    Determine if a string denotes a valid date YYYY-MM-DD.
    """
    return re.search("^[1-9]\d\d\d-\d\d-\d\d$", s)


def main():
    s = input("Enter a string (vowel): ")
    print(vowel(s))

    s = input("Enter a string (integer): ")
    print(num_int(s))

    s = input("Enter a string (YYYY-MM-DD): ")
    print(valid_date(s))


if __name__ == '__main__':
    main()
