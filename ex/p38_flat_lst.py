from functools import reduce


lst = [[1, 2], [3, 4], 5, [6], [[7], [8, 9]]]


def flatten(lst):
    def reducer(acc, val):
        # If val is a list, extend the accumulator with the flattened val
        if isinstance(val, list):
            acc.extend(flatten(val))
        else:
            # Otherwise, append the non-list item
            acc.append(val)
        return acc

    return reduce(reducer, lst, [])


x = flatten(lst)
print(x)
