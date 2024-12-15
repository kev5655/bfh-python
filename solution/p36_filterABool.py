def filter_A(lst):
    """Returns a list of booleans with True or False if a string starts with the letter 'A'"""
    res = []
    for e in lst:
        if e[0] == "A":
            res += [True]
        else:
            res += [False]
    return res

def filter_A2(lst):
    res =[]
    for e in lst:
        res += [ e[0] == "A" ]
    return res

def starts_with_A(s):
    return s[0] == "A"

def main():
    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
    print(filter_A(fruits))
    print(filter_A2(fruits))

    # with map and function
    map_elements = map(starts_with_A, fruits)
    print(list(map_elements))

    # filter with map and Lambda
    filter_elements = filter(starts_with_A, fruits)
    print(list(filter_elements))

if __name__ == "__main__":
    main()

