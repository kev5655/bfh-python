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
    print(f'dict min and max: {get_min_max_dict(
        {'a': 10, 'b': 5, 'c': 15, 'd': 7})}')
