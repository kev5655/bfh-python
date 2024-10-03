def flat_iterative(lst_lst: list[list[int]]) -> list[int]:
    """ Iterative function that flats a list of lists of integers."""
    res_lst = []
    for l in lst_lst:
        res_lst += l
    return res_lst


def flat_recursive(lst_lst: list[list[int]]) -> list[int]:
    """ Recursive function that flats a list of lists of integers."""
    if lst_lst == []:
        return []
    else:
        return lst_lst[0] + flat_recursive(lst_lst[1:])


def main():
    """ Launcher """
    input = [ [3, 4, 5], [10, 4], [], [6, 12, 4] ]

    # calls the iterative version
    output = flat_iterative(input)
    print(output)

    # calls the recursive version
    output = flat_recursive(input)
    print(output)

if __name__ == "__main__":
    main()
