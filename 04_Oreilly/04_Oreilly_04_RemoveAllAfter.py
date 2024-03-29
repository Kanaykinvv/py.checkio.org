# Не все элементы важны. Что вам здесь нужно сделать, так это удалить все элементы после данного из списка.
#
# 287 / 5000
# Результаты перевода
# Для иллюстрации у нас есть список [1, 2, 3, 4, 5], и нам нужно удалить все элементы,
# которые идут после 3, то есть 4 и 5.
#
# У нас есть два крайних случая:
# (1) если режущий элемент не может быть найден, то список не следует изменять;
# (2) если список пуст, он должен оставаться пустым.
#
# Вход: список и элемент границы.
#
# Вывод: итерируемый (кортеж, список, итератор ...).
#
# Example:
#
# remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
# remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]

from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    if len(items) > 0:
        if border in items:
            return items[0:items.index(border) + 1]
        else:
            return items
    else:
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
