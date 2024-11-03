
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


if __name__ == '__main__':
    print(f'sum it: {sum_it([1, 2, 3, 4, 5, 6, 7])}')
    print(f'sum rec: {sum_rec([1, 2, 3, 4, 5, 6, 7])}')
