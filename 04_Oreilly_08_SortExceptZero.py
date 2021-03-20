# Отсортируйте числа в массиве. Но положение нулей менять не стоит.
#
# nput: A List.
#
# Output: An Iterable (tuple, list, iterator ...).
#
# Example:
#
# except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# except_zero([0, 2, 3, 1, 0, 4, 5]) == [0, 1, 2, 3, 0, 4, 5]

from typing import Iterable


def except_zero(items: list) -> Iterable:
    # your code here
    list_zero = list()
    list_other = list()
    result = []

    for index in range(0, len(items)):
        if items[index] == 0:
            list_zero.append(index)
        else:
            list_other.append(items[index])

    list_other = sorted(list_other)

    a = 0 if len(list_other) > 0 else -1

    for i in range(0, len(items)):
        if i in list_zero:
            result.append(0)
        else:
            if a > -1:
                result.append(list_other[a])
                a += 1

    return result


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
