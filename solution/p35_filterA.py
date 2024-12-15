def starts_with_A(s):
    return s[0] == "A"

def main():
    fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
  
    # Filter function constructs an iterator from elements of an iterable for which a function returns true.

    # filter with function
    filter_elements = filter(starts_with_A, fruits)
    print(list(filter_elements))

    # filter with lambda
    filter_elements = filter(lambda s: s[0] == "A", fruits)
    print(list(filter_elements))

if __name__ == "__main__":
    main()

