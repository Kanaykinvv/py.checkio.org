# В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.
#
# example
#
# Входные данные: Список.
#
# Выходные данные: Набор элементов.
#
# Пример:
#
# replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# replace_first([1]) == [1]
from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) > 1:
        a = items[0]
        del items[0]
        items.append(a)
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
