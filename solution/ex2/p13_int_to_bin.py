

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

if __name__ == "main":
    print(f'int to binary list: {int_to_binary_bool_lst(1)}')
    print(f'int to binary list: {int_to_binary_bool_lst(2)}')
    print(f'int to binary list: {int_to_binary_bool_lst(3)}')
    print(f'int to binary list: {int_to_binary_bool_lst(4)}')
    print(f'int to binary list: {int_to_binary_bool_lst(5)}')
    print(f'int to binary list: {int_to_binary_bool_lst(6)}')
    print(f'int to binary list: {int_to_binary_bool_lst(7)}')