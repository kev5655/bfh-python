def max_without_built_in_max(dic: dict[str, int]) -> dict[str, int]:
    """
    Determine in a dictionary the entry (key, value) with max value.
    :param dic: the dictionary to consider
    :return: the entry (key, value) with the max value
    """
    max_key_value = ("", 0)

    for key, value in dic.items():
        if value > max_key_value[1]:
            max_key_value = (key, value)

    return max_key_value


def dic_with_min_max(dic: dict[str, int]) -> int:
    """
    Extract from a dictionary the two (key: value) elements for which value is the largest
    and smallest values whenever size of dictionary is greater or equal to 2.
    If size of the dictionary equal 1 the single pair is removed.
    If the dictionary is empty nothing is performed.
    :param dic: the dictionary to consider
    :return: the dictionary without the (key, value) elements for which value is max and min
    """
    # dictionaries are mutable data structures, so we have to work on a copy of the parameter
    # to avoid the modification of the dictionary passed as argument.
    # Doing a copy with  dic_copy = dic  is not enough because just the reference of the object dic
    # is copied.  Instead we have to use the function copy() or deepcopy().  Copy() performs a shallow
    # copy that copies the "first" level of the object, more precisely shallow copy constructs a new object
    # and inserts all the references of the original object. Deepcopy() constructs a new object and,
    # recursively, inserts deep copies of all the compound objects. For a more detailed description see
    # https://docs.python.org/3/library/copy.html#module-copy

    # In our situation a shallow copy works well because the elements of the dictionary are "simple" objects,
    # not compound objects.

    # Dictionary class is equipped of a copy() method that returns a shallow copy of the dictionary.
    dic_copy = dic.copy()

    if len(dic_copy) >= 2:  # normal case there are 2 or more pairs
        # to obtain the key of the max value we have to provide a function that returns the value of a key parameter
        # two ways are possible
        # first way: function provided as a lambda expression
        max_key = max(dic_copy, key=lambda k: dic_copy[k])
        # second way: function provided as the method get
        min_key = min(dic_copy, key=dic_copy.get)
        del dic_copy[max_key]
        del dic_copy[min_key]
    elif len(dic_copy) == 1:  # there is a single pair, just ignores it
        dic_copy = {}
    # if dic_copy is empty then does nothing
    return dic_copy


def main() -> None:
    """ Launcher """
    # a dictionary (name: age)
    pers_age = {'John': 44, 'Jane': 29, 'Jim': 72, 'Maria': 19, 'Oscar': 21, 'Dan': 28}
    # prints the whole dictionary
    print("The dictionary:", pers_age)
    # prints the size of the dictionary (number of pairs (key: value))
    print("Number of elements:", len(pers_age))
    # prints the value of a given key (two ways for the same thing)
    print("Age of Jane:", pers_age.get('Jane'))
    print("Age of Jane:", pers_age['Jane'])

    print("The entry (key, value) with max value of a dictionary:", max_without_built_in_max(pers_age))
    print("The dictionary without the two entries min and max:", dic_with_min_max(pers_age))

    # max returns the maximum value of an iterable (a data structure that can be iterated
    print("For dictionaries max returns the pair (key: value) with the max key:", max(pers_age))
    # to obtain the key of the max value we have to pass

    # calls the function and prints the result
    print("Entry (key, value) with max value:", dic_with_min_max(pers_age))
    # we observe that the initial dictionary is not modified
    print("Intial dictionary:", pers_age)


if __name__ == "__main__":
    main()
