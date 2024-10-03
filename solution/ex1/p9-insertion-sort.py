def insert_ord(num, lst):
    """
    Inserts at the right place a number into an ordered list (ascending order).
    This version update the parameter list and is written in a pythonic way.  
    :param num: the number to add in the list
    :param lst: the ordered list in which num has to be added
    :return: none
    """
    if not lst:  # check if the list is empty
        return lst.insert(0, num)  # insert num
    else:
        if num >= lst[len(lst) - 1]:  # check if num is greater than every thing
            lst.append(num)  # append num to the list (after all the elements)
        else:
            for index in range(len(lst)):  # loop over the whole list
                if num <= lst[index]:  # check if num is smaller than the current position
                    lst.insert(index, num)  # insert before
                    break  # quit the for loop


def insertion_sort(unordered):
    """
    Sorts an unordered list of numbers in ascending order using insertion sort technique
    :param unordered: the unsorted list to sort
    :return: the sorted list in ascending order
    """
    ordered = []
    for num in unordered:
        insert_ord(num, ordered)
    return ordered


def main():
    """ Launcher """
    lst = [10, 3, -4, 20, 3, 9, -1]
    insertion_sort(lst)
    print("The ordered list {}".format(insertion_sort(lst)))


if __name__ == "__main__":
    main()
