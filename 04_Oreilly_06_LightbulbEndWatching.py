# В третьей миссии из серии о лампочках я хочу выделить отдельно процесс, а отдельно период наблюдения за этим
# процессом.
#
# В предыдущей миссии был введен параметр start_watching, а в этой – end_watching, который указывает время окончания
# наблюдения. Если он не передан, миссия работает, как и в предыдущей версии, без ограничения времени наблюдения.
#
# Еще одно изменение в том, что количество элементов (нажатий на кнопку) может быть нечетным (в предыдущей миссии
# серии - количество элементов всего было четным).
#
# example
#
# Input: Три аргумента и только первый обязательный. Первый – a list of datetime objects, а второй и
# третий – the datetime objects.
#
# Output: Количество секунд как integer.
#
# Example:
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
# ],
# datetime(2015, 1, 12, 10, 10, 0),
# datetime(2015, 1, 12, 11, 0, 10)) == 20
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
# ],
# datetime(2015, 1, 12, 9, 9, 0),
# datetime(2015, 1, 12, 10, 0, 0)) == 0
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ],
# datetime(2015, 1, 12, 9, 0, 0),
# datetime(2015, 1, 12, 10, 5, 0)) == 300

# Предусловия:
#
# Массив нажатий на кнопку всегда отсортирован по возрастанию
# В массиве нажатий на кнопку нет повторяющихся элементов
# Минимально возможная дата 1970-01-01
# Максимально возможная дата 9999-12-31
# Taken from mission Lightbulb Start Watching

# Taken from mission Lightbulb Intro
from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    seconds = 0

    if len(els) % 2 > 0:
        els_1 = els[:-1]
        els_2 = els[-1:]
    else:
        els_1 = els[:]
        els_2 = None

    for index in range(0, len(els_1)-1, 2):
            if start_watching != None:
                if start_watching >= els_1[index + 1]:
                    start = els_1[index + 1]
                elif (start_watching > els_1[index]) and (start_watching < els_1[index + 1]):
                    start = start_watching
                else:
                    start = els_1[index]
            else:
                start = els_1[index]

            if end_watching != None:
                if end_watching >= els_1[index + 1]:
                    finish = els_1[index + 1]
                elif (end_watching > els_1[index]) and (end_watching < els_1[index + 1]):
                    finish = end_watching
                else:
                    finish = els_1[index]
            else:
                finish = els_1[index + 1]

            all_time = finish - start
            seconds += all_time.total_seconds()

    if els_2 and len(els_2) > 0:
        if start_watching != None:
            start = start_watching if start_watching > els_2[0] else els_2[0]
        else:
            start = els_2[0]

        if end_watching != None:
            finish = end_watching if end_watching > els_2[0] else els_2[0]
        else:
            finish = els_2[0]

        all_time = finish - start
        seconds += all_time.total_seconds()

    return seconds


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 1, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 0),
        end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 7)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 3),
        datetime(2015, 1, 12, 10, 0, 10)) == 7

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
        datetime(2015, 1, 12, 10, 0, 10),
        datetime(2015, 1, 12, 10, 0, 20)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 30, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 50, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 9, 0, 0),
        datetime(2015, 1, 12, 10, 5, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 12, 0, 0)) == 310

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 11, 5, 0),
        datetime(2015, 1, 12, 11, 10, 0)) == 300

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 10, 10, 0),
        datetime(2015, 1, 12, 11, 0, 10)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 10, 0),
        datetime(2015, 1, 12, 10, 20, 20)) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 0)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
    ],
        datetime(2015, 1, 12, 9, 9, 0),
        datetime(2015, 1, 12, 10, 0, 10)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10)
    ]) == 1220

    print("The third mission in series is completed? Click 'Check' to earn cool rewards!")