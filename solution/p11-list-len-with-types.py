# It is very convenient to add type information at least for function parameters and return value
# The description of parameters and return value is also possible.

def list_len(lst: list[str]) -> list[int]:   # typing of parameter and return value
    """
    Takes a list of strings and returns a list of integers where
    the values are the length of each string.
    :param lst: input list of strings.
    :return: list containing the length of each element of the input list.
    """
    res_lst = []
    for s in lst:
        res_lst += [len(s)]
    return res_lst


def main():
    """ Launcher """
    lst_strings: list[str] = ["hello", "hi", "Python"]    # introduction of type for variables
    print(list_len(lst_strings))


if __name__ == '__main__':
    main()
