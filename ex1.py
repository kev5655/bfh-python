import math


# 4
def is_even(n):
    return n % 2 == 0


# 5
def circle_area(r):
    return math.pi * r * r


# 6
def get_greatest(lst):
    return max(lst)


# 7
def reverse_it(lst):
    new_lst = []
    for i in range(len(lst)):
        item = lst[-1 - i]
        new_lst.append(item)
    return new_lst


# 7
def reverse_rec(lst):
    a, b = lst[0], lst[-1]
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        return [b, a]
    return [b] + reverse_rec(lst[1:-1]) + [a]


# 8
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


# 8
def insert_sorted_asc(lst, n):
    return reverse_rec(insert_sorted(lst, n))


# 9
def insert_ordered(lst, num):
    lst.append(num)
    lst.sort()  # This ensures the list stays ordered
    return lst


# 10
def sum_it(lst):
    s = 0
    for l in lst:
        if type(l) is int:
            s += l
    return s


# 10
def sum_rec(lst):
    if len(lst) == 0:
        return 0
    return sum_it(lst[1:]) + lst[0]


# 11
def count_words_len(lst):
    counts = []
    for l in lst:
        if type(l) is str:
            count = 0
            for _ in l:
                count += 1
            counts.append(count)
        else:
            counts.append(0)
    return counts


# 12
def flat(dlst):
    result = []
    for lst in dlst:
        if type(lst) is list:
            result = result + flat(lst)
        else:
            result.append(lst)
    return result


if __name__ == '__main__':
    print(f'is 10 even {is_even(10)}')
    print(f'is 11 even {is_even(11)}')

    print(f'area of 12: {circle_area(12)}')

    print(f'get greatest: {get_greatest([10, 12, 13, 44, 20, 1, 99, 100])}')

    print(f'reverse list: {reverse_it([10, 12, 13, 44, 20, 1, 99, 100])}')
    print(f'reverse list: {reverse_rec([10, 12, 13, 44, 20, 1, 99, 100])}')

    print(f'in sorted: {insert_sorted([1, 2, 3, 4, 5, 6, 7], 4)}')
    print(f'in sorted: {insert_sorted([1, 2, 3, 5, 6, 7], 4)}')

    print(f'in sorted asc: {insert_sorted_asc([1, 2, 3, 5, 6, 7], 4)}')

    print(f'in insert_ordered: {insert_ordered([3, 7, 2, 6, 1, 5], 4)}')

    print(f'sum it: {sum_it([1, 2, 3, 4, 5, 6, 7])}')
    print(f'sum rec: {sum_rec([1, 2, 3, 4, 5, 6, 7])}')

    print(f'count words {count_words_len(["welcome", "to", "the", "jungle"])}')

    print(f'flat int: {flat([[3, 8], [8, 9, 9], [1, 2]])}')
    print(f'flat str: {flat([["ab", "c"], ["d", "ef"]])}')
