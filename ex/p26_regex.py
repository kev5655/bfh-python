import re


def contains_vowel(text: str):
    x = re.search("vowel", text)
    return x != None


def is_number(text: str):
    x = re.fullmatch(r'\d+', text)
    return x != None


def is_date(text: str):
    x = re.fullmatch(
        r'(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])', text)
    return x != None


def main():
    print(contains_vowel("Hallo"))
    print(contains_vowel("Halvowello"))
    print()
    print(is_number("123"))
    print(is_number("abc"))
    print(is_number("12a3"))
    print(is_number(""))
    print()

    # Example usage with print statements
    print(is_date("2024-12-09"))  # True, valid date format
    print(is_date("2024-02-30"))  # True, matches regex but not a valid date
    print(is_date("2024-00-09"))  # False, month 00 is invalid
    print(is_date("2024-13-09"))  # False, month 13 is invalid
    print(is_date("2024-12-32"))  # False, day 32 is invalid
    print(is_date("abcd-12-09"))  # False, invalid year
    print(is_date(""))            # False, empty string


if __name__ == "__main__":
    main()
