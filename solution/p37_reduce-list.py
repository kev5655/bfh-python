import functools
from operator import mul


def product(lst: list[int]) -> int:
    """
    Returns the product of a list of integers using the higher-order function reduce.

    :param lst the list of integers to consider
    :return the product of the list of integers
    """
    return functools.reduce(lambda a, b: a * b, lst)


def product2(lst: list[int]) -> int:
    """
    Returns the product of a list of integers using the higher-order function reduce and
    the mul operator that has to be imported instead of a lambda.

    :param lst the list of integers to consider
    :return the product of the list of integers
    """
    return functools.reduce(mul, lst)


def multi(a: int, b: int) -> int:
    return a * b


def product3(lst: list[int]) -> int:
    """
    Returns the product of a list of integers using the higher-order function reduce and
    the defined multi() function.

    :param lst the list of integers to consider
    :return the product of the list of integers
    :param lst:
    :return:
    """
    return functools.reduce(multi, lst)


def factorial(n: int) -> int:
    return functools.reduce(mul, range(1, n + 1))


def main():
    list_of_numbers = [1, 2, 3, 4, 5]
    print(product(list_of_numbers))

    print(product2(list_of_numbers))

    print(product3(list_of_numbers))

    print(factorial(5))


if __name__ == "__main__":
    main()

