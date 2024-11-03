# 9
def insert_ordered(lst, num):
    lst.append(num)
    lst.sort()  # This ensures the list stays ordered
    return lst


if __name__ == '__main__':
    print(f'in insert_ordered: {insert_ordered([3, 7, 2, 6, 1, 5], 4)}')
