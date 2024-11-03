from typing import Iterable
from typing import TypeVar, List


# 11
def count_words_len(lst: list[str]) -> list[str]:
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


type ListIntStr = list[str | int | Iterable[ListIntStr]]


# 12
def flat(dlst: ListIntStr):
    result = []
    for lst in dlst:
        if type(lst) is list:
            result = result + flat(lst)
        else:
            result.append(lst)
    return result


# 13
def int_to_binary_bool_lst(i: int) -> list[bool]:
    if i > 7:
        return []
    binary = bin(i).replace('0b', '')
    boolList = []
    for i in binary:
        match i:
            case "0":
                boolList.append(False)
            case "1":
                boolList.append(True)
    return boolList


# 14
def int_list_to_binary_bool_lst(lst: list[int]) -> list[list[bool]]:
    result = []
    for i in lst:
        result.append(int_to_binary_bool_lst(i))
    return result


# 15
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

# 16
def get_min_max_dict(dic: dict[str, int]) -> dict[str, int]:
    mi_dict, mx_dict = {"x": 99999}, {"x": 0}
    result: dict[str, int] = {}
    for k, v in dic.items():
        if v < list(mi_dict.values())[0]:
            del mi_dict[list(mi_dict.keys())[0]]
            mi_dict[k] = v
        if v > list(mx_dict.values())[0]:
            del mx_dict[list(mx_dict.keys())[0]]
            mx_dict[k] = v

    return mi_dict | mx_dict


if __name__ == '__main__':
    print(f'count words {count_words_len(["welcome", "to", "the", "jungle"])}')

    print(f'flat int: {flat([[3, 8], [8, 9, 9], [1, 2]])}')
    print(f'flat str: {flat([["ab", "c"], ["d", "ef"]])}')

    print(f'int to binary list: {int_to_binary_bool_lst(1)}')
    print(f'int to binary list: {int_to_binary_bool_lst(2)}')
    print(f'int to binary list: {int_to_binary_bool_lst(3)}')
    print(f'int to binary list: {int_to_binary_bool_lst(4)}')
    print(f'int to binary list: {int_to_binary_bool_lst(5)}')
    print(f'int to binary list: {int_to_binary_bool_lst(6)}')
    print(f'int to binary list: {int_to_binary_bool_lst(7)}')

    print(f'int list to binary list: {int_list_to_binary_bool_lst([1, 2, 3, 4, 5, 6, 7])}')

    print(f'merge col and row: {merge_col_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}')
    try:
        merge_col_row([[1, 2, 3], [4, 5, 6], [7, 8]])
    except ValueError:
        print('ValueError pass')

    print(f'dict min and max: {get_min_max_dict({'a': 10, 'b': 5, 'c': 15, 'd': 7})}')
