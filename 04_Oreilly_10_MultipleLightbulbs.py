# В 4ой миссии серии добавляется больше лампочек.
#
# Все также надо определить, как долго будет освещена комната в период наблюдения между start_watching и end_watching.
# Но теперь у нас более одной лампочки. А значит в массиве переключения лампочек теперь может быть передан еще и номер
# лампочки, кнопка которой нажимается.
#
# Каждым элементом массива нажатий на кнопку может быть или объект datetime (значит время нажатия на первую кнопку)
# или tuple из 2х элементов (где первый элементы — это объект datetime время нажатия на кнопку), а второй это номер
# лампочки, кнопка который нажимается.
#
# Если переданный массив будет состоять только из элементов datetime, то значит у нас только одна лампочка и функция
# должна работать также, как и в предыдущей миссии серии.
#
# example
#
# Input: Три аргумента и только первый обязательный. Первый – a list of datetime objects(вместо datetime может быть
# [datetime, int]), а второй и третий – the datetime objects.
#
# Output: Количество секунд как integer.
# Предусловия:
#
# Массив нажатий на кнопку всегда отсортирован по возрастанию
# В массиве нажатий на кнопку нет повторяющихся элементов
# Количество элементов всегда четное число (это значит, что лампочка, в конце концов, будет выключена)
# Минимально возможная дата 1970-01-01
# Максимально возможная дата 9999-01-01

from datetime import datetime
from typing import List


def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    seconds = 0
    for index in range(0, len(els) - 1, 2):
        all_time = els[index + 1] - els[index]
        seconds += all_time.total_seconds()
    return seconds
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ]))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#     ]) == 610
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ]) == 1220
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 12, 10, 10),
#     ]) == 4820
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 1),
#     ]) == 1
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 13, 11, 0, 0),
#     ]) == 86410
#
#     print("The first mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    seconds = 0

    for index in range(0, len(els) - 1, 2):
        if start_watching != None:
            if start_watching < els[index]:
                all_time = els[index + 1] - els[index]
                seconds += all_time.total_seconds()
            elif (els[index + 1] - start_watching).total_seconds() > 0:
                all_time = els[index + 1] - start_watching
                seconds += all_time.total_seconds()
        else:
            all_time = els[index + 1] - els[index]
            seconds += all_time.total_seconds()
    return seconds

#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         datetime(2015, 1, 12, 10, 0, 5)))
#
#     assert sum_light(els=[
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ], datetime(2015, 1, 12, 10, 0, 0)) == 10
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ], datetime(2015, 1, 12, 11, 0, 0)) == 610
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ], datetime(2015, 1, 12, 11, 0, 10)) == 600
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ], datetime(2015, 1, 12, 10, 10, 0)) == 620
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 11, 10, 11),
#         datetime(2015, 1, 12, 12, 10, 11),
#     ], datetime(2015, 1, 12, 12, 10, 11)) == 0
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#         datetime(2015, 1, 12, 11, 10, 11),
#         datetime(2015, 1, 12, 12, 10, 11),
#     ], datetime(2015, 1, 12, 12, 9, 11)) == 60
#
#     print("The second mission in series is done? Click 'Check' to earn cool rewards!")

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

    for index in range(0, len(els_1) - 1, 2):
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
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10)))
#
#     assert sum_light(els=[
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         start_watching=datetime(2015, 1, 12, 10, 0, 0),
#         end_watching=datetime(2015, 1, 12, 10, 0, 10)) == 10
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 7)) == 7
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         datetime(2015, 1, 12, 10, 0, 3),
#         datetime(2015, 1, 12, 10, 0, 10)) == 7
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ],
#         datetime(2015, 1, 12, 10, 0, 10),
#         datetime(2015, 1, 12, 10, 0, 20)) == 0
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 10, 30, 0),
#         datetime(2015, 1, 12, 11, 0, 0)) == 0
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 10, 10, 0),
#         datetime(2015, 1, 12, 11, 0, 0)) == 10
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 10, 10, 0),
#         datetime(2015, 1, 12, 11, 0, 10)) == 20
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 9, 50, 0),
#         datetime(2015, 1, 12, 10, 0, 10)) == 10
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 9, 0, 0),
#         datetime(2015, 1, 12, 10, 5, 0)) == 300
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#         datetime(2015, 1, 12, 11, 10, 10),
#     ],
#         datetime(2015, 1, 12, 11, 5, 0),
#         datetime(2015, 1, 12, 12, 0, 0)) == 310
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#     ],
#         datetime(2015, 1, 12, 11, 5, 0),
#         datetime(2015, 1, 12, 11, 10, 0)) == 300
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#     ],
#         datetime(2015, 1, 12, 10, 10, 0),
#         datetime(2015, 1, 12, 11, 0, 10)) == 20
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 10, 10),
#         datetime(2015, 1, 12, 11, 0, 0),
#     ],
#         datetime(2015, 1, 12, 9, 10, 0),
#         datetime(2015, 1, 12, 10, 20, 20)) == 610
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#     ],
#         datetime(2015, 1, 12, 9, 10, 0),
#         datetime(2015, 1, 12, 10, 20, 20)) == 1220
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#     ],
#         datetime(2015, 1, 12, 9, 9, 0),
#         datetime(2015, 1, 12, 10, 0, 0)) == 0
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#     ],
#         datetime(2015, 1, 12, 9, 9, 0),
#         datetime(2015, 1, 12, 10, 0, 10)) == 10
#
#     print("The third mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
              start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    def sum_light_only(els: List[datetime]) -> int:
        seconds = 0
        for index in range(0, len(els) - 1, 2):
            all_time = els[index + 1] - els[index]
            seconds += all_time.total_seconds()
        return seconds

    def sum_light_start(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
        """
            how long the light bulb has been turned on
        """
        seconds = 0

        for index in range(0, len(els) - 1, 2):
            if start_watching != None:
                if start_watching < els[index]:
                    all_time = els[index + 1] - els[index]
                    seconds += all_time.total_seconds()
                elif (els[index + 1] - start_watching).total_seconds() > 0:
                    all_time = els[index + 1] - start_watching
                    seconds += all_time.total_seconds()
            else:
                all_time = els[index + 1] - els[index]
                seconds += all_time.total_seconds()
        return seconds

    def sum_light_start_stop(els: List[datetime], start_watching: Optional[datetime] = None,
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

        for index in range(0, len(els_1) - 1, 2):
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

    # Количество секунд освещение комнаты
    seconds = 0

    # Максимальное количество лампочек (по-умолчанию 1)
    max_light = 1

    # Список состояния лампочек
    lights = list()

    # Поиск максимального количества лампочек
    for el in els:
        if type(el) == tuple:
            if max_light < el[1]:
                max_light = el[1]

    print("Максимум лампочек = " + str(max_light))

    # Заполняем весь список состоянию лампочек как выключенные
    for i in range(0, max_light):
        lights[i] = False




    #
    # for el in els:
    #     if type(el) == datetime:
    #
    #         # if ligths[0] == False:
    #         #     ligths[0] = True
    #         # else:
    #         #     ligths[0] = False
    #
    #     elif type(el) == tuple:










if __name__ == '__main__':
    print("Example:")

    print(sum_light(els=[
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 0), end_watching=datetime(2015, 1, 12, 10, 1, 0)))

    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ]) == 60
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 11, 0, 0), 2),
    #     (datetime(2015, 1, 12, 11, 1, 0), 2),
    # ]) == 70
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ]) == 30
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ]) == 40
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    #     (datetime(2015, 1, 12, 10, 1, 0), 3),
    #     (datetime(2015, 1, 12, 10, 1, 20), 3),
    # ]) == 60
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], datetime(2015, 1, 12, 10, 0, 50)) == 10
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 30)) == 20
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 20)) == 30
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 10)) == 30
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 50)) == 0
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 30)) == 20
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 20)) == 30
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    #     (datetime(2015, 1, 12, 10, 1, 20), 2),
    #     (datetime(2015, 1, 12, 10, 1, 40), 2),
    # ], datetime(2015, 1, 12, 10, 0, 20)) == 50
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     datetime(2015, 1, 12, 10, 0, 10),
    # ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30)) == 30
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     datetime(2015, 1, 12, 10, 0, 40),
    #     (datetime(2015, 1, 12, 10, 0, 50), 2),
    # ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20
    #
    # assert sum_light(els=[
    #     (datetime(2015, 1, 11, 0, 0, 0), 3),
    #     datetime(2015, 1, 12, 0, 0, 0),
    #     (datetime(2015, 1, 13, 0, 0, 0), 3),
    #     (datetime(2015, 1, 13, 0, 0, 0), 2),
    #     datetime(2015, 1, 14, 0, 0, 0),
    #     (datetime(2015, 1, 15, 0, 0, 0), 2),
    # ], start_watching=datetime(2015, 1, 10, 0, 0, 0), end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600
    #
    # print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")
