def reverse_rec(lst):
    """Reverse a given list of elements (recursive version)"""
    
    if lst == []:
        return []
    else:
        head, tail = lst[0], lst[1:]
        return reverse_rec(tail) + [head]


def main():
    """ Launcher """
    lst = [55,65,3,7]
    print("The reverse of {} is {}.".format(lst, reverse_rec(lst)))


if __name__ == "__main__":
    main()
