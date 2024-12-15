from functools import reduce

int_lst = [2, 4, 7]


def count_up(a, b):
    return a + b


mx = reduce(count_up, int_lst, 0)
print(mx)

mx = reduce(lambda a, b: a + b, int_lst, 0)
print(mx)
