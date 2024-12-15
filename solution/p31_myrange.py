class MyRange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
        
def main():
    """ Launcher """

    myrange = MyRange(10)
    # myrange is an iterable data structure
    # we can use it directly as an iterator

    for r in myrange:
       print(r)

    print("---")

    # or we can invoke iter() to receive an iterator
    myrange2 = MyRange(10)
    it = iter(myrange2)

    for r in it:
        print(r)
    
    # we observe that the iterator is a  one shoot object
    # we cannot use it twice on the same object

    # another observation is that the for loop catches
    # the StopIteration for your convenience

    print("---")

    # we can also iterate the elements in a while loop
    # and catch the StopIteration exception

    myrange3 = MyRange(10)
    it = iter(myrange3)
    
    while True:
        try:
            element = next(it)
            print(element)
        except StopIteration:
            break

if __name__ == "__main__":
    main()
