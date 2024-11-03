from typing import Iterable


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


if __name__ == '__main__':
    print(f'flat int: {flat([[3, 8], [8, 9, 9], [1, 2]])}')
    print(f'flat str: {flat([["ab", "c"], ["d", "ef"]])}')
