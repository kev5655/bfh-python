from functools import reduce

def add(x, y):
    return x + y

def main():
    lst = [[2, 4, 7, 3], [], ["a", "b"]]

    # with function
    print(reduce(add, lst))
          
    # with lambda
    print(reduce(lambda x, y: x + y, lst))

if __name__ == "__main__":
    main()

