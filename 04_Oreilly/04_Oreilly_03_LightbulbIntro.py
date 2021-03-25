# На вход функции дан массив datetime объектов — это дата и время нажатия на кнопку. Вашей задачей является определить,
# как долго горела лампочка. Массив при этом всегда отсортирован по возрастанию, в нем нет повторяющихся элементов и
# количество элементов всегда четное число (это значит, что лампочка, в конце концов, будет выключена).
#
# Input: A list of datetime objects
#
# Output: Колличество секунд как integer.
#
# Example:
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 10 , 10),
# ]) == 610
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 10 , 10),
#     datetime(2015, 1, 12, 11, 0 , 0),
#     datetime(2015, 1, 12, 11, 10 , 10),
# ]) == 1220
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 0 , 1),
# ]) == 1
#
# Предусловия:
#
# Массив нажатий на кнопку всегда отсортирован по возрастанию.
# В массиве нажатий на кнопку нет повторяющихся элементов (это значит, что результат всегда больше нуля).
# Количество элементов всегда четное число (это значит, что лампочка, в конце концов, будет выключена).
# Минимально возможная дата 1970-01-01
# Максимально возможная дата 202020-01-01
from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    seconds = 0
    for index in range(0, len(els)-1, 2):
        all_time = els[index+1] - els[index]
        seconds += all_time.total_seconds()
    return seconds


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 12, 10, 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 13, 11, 0, 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")