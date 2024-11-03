

# 15
from typing import List, TypeVar


T = TypeVar('T')


def merge_col_row(lst: list[list[T]]) -> List[List[T]]:
    lenLst = [len(l) for l in lst]
    mx, mi = max(lenLst), min(lenLst)
    if mx != mi:
        raise ValueError("not every list are has the same length")

    result: List[List[T]] = [[] for _ in range(0, len(lst[0]))]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            element = lst[i][j]
            result[j].append(element)

    return result


if __name__ == '__main__':
    print(f'merge col and row: {merge_col_row(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]])}')
    try:
        merge_col_row([[1, 2, 3], [4, 5, 6], [7, 8]])
    except ValueError:
        print('ValueError pass')
