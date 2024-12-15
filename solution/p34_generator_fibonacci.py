def fibonacci():
    """A generator for the infinite Fibonacci serie
       Fib[0] = 0
       Fib[1] = 1
       Fib[n+2] = Fib[n] + Fib[n+1]
    """
    f1 = 0
    yield f1
    f2 = 1
    yield f2
    while True:
        f3 = f1 + f2
        yield f3
        f1 = f2
        f2 = f3


def main():
    """ Launcher """
    # Every generator is also an iterator (not vice-versa)
    # function fibonacci() is a generator, calling fibonacci() returns
    # a generator. gen is a generator and therefore also an iterator.
    gen = fibonacci()
    for _ in range(15):
        print(next(gen))


if __name__ == "__main__":
    main()

