def reverse(lst):
    """Reverses the given list and returns it"""
    res_list = []
    for elem in lst:
        res_list = [elem] + res_list
    return res_list


def main():
    """ Launcher """
    lst = [67, 88, 123, 4]
    print("The reverse of {} is {}.".format(lst, reverse(lst)))


if __name__ == "__main__":
    main()
