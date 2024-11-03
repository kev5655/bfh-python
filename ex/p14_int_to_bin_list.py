from p13_int_to_bin import int_to_binary_bool_lst


# 14
def int_list_to_binary_bool_lst(lst: list[int]) -> list[list[bool]]:
    result = []
    for i in lst:
        result.append(int_to_binary_bool_lst(i))
    return result


if __name__ == '__main__':
    print(f'int list to binary list: {
          int_list_to_binary_bool_lst([1, 2, 3, 4, 5, 6, 7])}')
