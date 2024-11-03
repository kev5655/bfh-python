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


if __name__ == '__main__':
    print(f'reverse list: {reverse_it([10, 12, 13, 44, 20, 1, 99, 100])}')
    print(f'reverse list: {reverse_rec([10, 12, 13, 44, 20, 1, 99, 100])}')
