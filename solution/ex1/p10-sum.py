def sum2(lst):
    """Computes the sum of the list of integers"""
    s = 0
    for x in lst:
        s += x
    return s


def sum3(lst):
    """Computes the sum of the list of integers (recursive version)"""
    if not lst:
        return 0                        # 0 when list is empty
    else:
        return (lst[0] + sum3(lst[1:])) # head of list + sum of the tail otherwise


def main():
    """ Launcher """
    print(sum3([2,5,7,1]))

if __name__ == "__main__":
    main()
