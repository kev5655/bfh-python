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


if __name__ == '__main__':
    print(f'count words {count_words_len(["welcome", "to", "the", "jungle"])}')
