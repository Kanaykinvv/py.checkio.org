# Разделите список на более мелкие списки одинакового размера (куски). Последний фрагмент может быть меньше размера
# фрагмента по умолчанию. Если список пуст, значит, у вас вообще не должно быть чанков.

# Input: Two arguments. A List and chunk size.
#
# Output: An Iterable with chunked Iterable.
#
# Example:
#
# chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
# chunking_by([3, 4, 5], 1) == [[3], [4], [5]]
# Precondition: chunk-size > 0

from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    """
    Функция разбиения входного списка на списки заданной длины
    :param items: Входной список
    :param size: Ограничение длины
    :return: Результирующий список списков ограниченной длины
    """
    result = list()
    tmp_list = list()

    for index in range(len(items)):
        tmp_list.append(items[index])
        if (len(tmp_list) % size == 0) or (index == len(items) - 1):
            result.append(tmp_list.copy())
            tmp_list.clear()

    return result

if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
