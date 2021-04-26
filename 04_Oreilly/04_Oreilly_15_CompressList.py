# A given list should be "compressed" in a way so, instead of two (or more) equal elements, staying one after another,
# there is only one in the result Iterable (list, tuple, iterator ...).
# Данный список должен быть «сжат» таким образом, чтобы вместо двух (или более) равных элементов,
# стоящих один за другим, в результате Iterable был только один (список, кортеж, итератор ...).
#
# example
#
# Input: List.
#
# Output: "Compressed" Iterable (list, tuple, iterator ...).
#
# Example:
#
# compress([
#   5, 5, 5,
#   4, 5, 6,
#   6, 5, 5,
#   7, 8, 0,
#   0]) == [5, 4, 5, 6, 5, 7, 8, 0]
# compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]) == [1, 2, 1]

from typing import Iterable

def compress(items: list) -> Iterable:
    """
    Функция для сжимания списка
    :param items: Входной список
    :return: Сжатый список
    """
    # Результирующий список
    result = []
    # Список индексов различающихся элементов входного списка
    link_list = []

    # Если входной список состоит из 1 элемента
    if len(items) == 1:
        # Результат будет сам входной список
        result = items
    # Если писок имеет длину больше 1
    elif len(items) > 1:
        # Проходим весь входной список (без последнего индекса)
        for index in range(len(items) - 1):
            # Если индекс списка последний
            if index + 1 == len(items) - 1:
                # Проверяем равенство последнего и предпоследнего элементов
                if items[index] == items[index + 1]:
                    # Если равны, заносим один индекс
                    link_list.append(index)
                else:
                    # Иначе заносим оба индекса
                    link_list.append(index)
                    link_list.append(index + 1)
            # Если индекс не последний, проверяем равенство текущего элемента и следующего
            elif items[index] != items[index + 1]:
                # При их различии, запоминаем позицию текущего элемента
                link_list.append(index)

        # Формируем окончательный список исходя из запомненных позиций
        for link in link_list:
            result.append(items[link])

    return result

if __name__ == '__main__':
  #   print("Example:")
  #   print(list(compress([
  # 5, 5, 5,
  # 4, 5, 6,
  # 6, 5, 5,
  # 7, 8, 0,
  # 0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    print("Coding complete? Click 'Check' to earn cool rewards!")
