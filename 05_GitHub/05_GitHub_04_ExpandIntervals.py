# Интервал последовательных положительных целых чисел можно кратко описать как кортеж, содержащий первое и
# последнее значения. Например, интервал, содержащий числа 5, 6, 7, 8, 9, можно описать как (5,9). Несколько
# интервалов можно объединить в повторяемые. Учитывая итерацию с интервалами (гарантированно не перекрывающуюся друг
# с другом и перечисленную в отсортированном порядке возрастания), создайте и верните список, содержащий все целые
# числа, содержащиеся в этих интервалах.

#
# An interval of consecutive positive integers can be succinctly described as a tuple that contains first and last
# values. For example, the interval that contains the numbers 5, 6, 7, 8, 9 can be described as (5,9). Multiple
# intervals can be united together into iterable. Given an an iterable with intervals (guaranteed not to overlap
# with each other and to be listed in a sorted ascending order), create and return the list that contains all the
# integers contained by these intervals.
#
# Input: The iterable of tuples of two integers.
#
# Output: The iterable of integers.
#
# Example:
#
# expand_intervals([(1, 3), (5, 7)]) == [1, 2, 3, 5, 6, 7]
# expand_intervals([(1, 3)]) == [1, 2, 3]

from typing import Iterable

def expand_intervals(items: Iterable) -> Iterable:
    """
    Функция определения всех знацений по предоставленным отрезкам.
    :param items: Список отрезвов
    :return: Все входящие значения по отрезкам с сортировкой
    """
    result_set = set()

    # Если список не пустой
    if len(items) > 0:
        # Перебираем его и генерируем новый от минимального до максимального значения,
        # с добавлением/обновлением этих значений в исходное множество
        for item in items:
            result_set.update(list(range(min(item), max(item) + 1)))
        # По окончании формируем отсортированный список исходя из полученного множества
        return sorted(list(result_set))
    else:
        # Если исходный список пустой - возвращаем пустой список
        return []


if __name__ == '__main__':
    print("Example:")
    print(list(expand_intervals([(1, 3), (5, 7)])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(expand_intervals([(1, 3), (5, 7)])) == [1, 2, 3, 5, 6, 7]
    assert list(expand_intervals([(1, 3)])) == [1, 2, 3]
    assert list(expand_intervals([])) == []
    assert list(expand_intervals([(1, 2), (4, 4)])) == [1, 2, 4]
    print("Coding complete? Click 'Check' to earn cool rewards!")
