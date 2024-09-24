import math

from decorator import append


def is_even(n):
    return n % 2 == 0


def circle_area(r):
    return math.pi * r ** 2


def get_greatest(lst):
    return max(lst)


def reverse_it(lst):
    new_lst = []
    for i in range(len(lst)):
        item = lst[-1 - i]
        new_lst.append(item)
    return new_lst


def reverse_rec(lst):
    a, b = lst[0], lst[-1]
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        return [b, a]
    return [b] + reverse_rec(lst[1:-1]) + [a]


def insert_sorted(lst, n):
    if len(lst) == 0:
        return [n]
    if len(lst) == 1:
        if n < lst[0]:
            return [n] + lst
        else:
            return lst + [n]

    middle = len(lst) // 2
    if n < lst[middle]:
        return insert_sorted(lst[0:middle], n) + lst[middle:]
    else:
        return lst[:middle] + insert_sorted(lst[middle:], n)

def insert_sorted_asc(lst, n):
    return reverse_rec(insert_sorted(lst, n))

def sort(lst):


if __name__ == '__main__':
    print(f'is 10 even {is_even(10)}')
    print(f'is 11 even {is_even(11)}')

    print(f'area of 12: {circle_area(12)}')

    print(f'get greatest: {get_greatest([10, 12, 13, 44, 20, 1, 99, 100])}')

    print(f'reverse list: {reverse_it([10, 12, 13, 44, 20, 1, 99, 100])}')
    print(f'reverse list: {reverse_rec([10, 12, 13, 44, 20, 1, 99, 100])}')

    print(f'in sorted: {insert_sorted([1,2,3,4,5,6,7], 4)}')
    print(f'in sorted: {insert_sorted([1,2,3,5,6,7], 4)}')

    print(f'in sorted asc: {insert_sorted_asc([1, 2, 3, 5, 6, 7], 4)}')

