from typing import Iterable


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

type ListIntStr = list[str|int|Iterable[ListIntStr]]

# 12
def flat(dlst: ListIntStr):
    result = []
    for lst in dlst:
        if type(lst) is list:
            result = result + flat(lst)
        else:
            result.append(lst)
    return result

# 13 Todo
# 14 Todo
# 15 Todo

if __name__ == '__main__':
    print(f'count words {count_words_len(["welcome", "to", "the", "jungle"])}')

    print(f'flat int: {flat([[3, 8], [8, 9, 9], [1, 2]])}')
    print(f'flat str: {flat([["ab", "c"], ["d", "ef"]])}')
