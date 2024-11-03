from p7_reverse import reverse_rec

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


if __name__ == '__main__':
    print(f'in sorted: {insert_sorted([1, 2, 3, 4, 5, 6, 7], 4)}')
    print(f'in sorted: {insert_sorted([1, 2, 3, 5, 6, 7], 4)}')

    print(f'in sorted asc: {insert_sorted_asc([1, 2, 3, 5, 6, 7], 4)}')
