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

    # Количество секунд освещение комнаты
    seconds = 0

    # Максимальное количество лампочек (по-умолчанию 1)
    max_light = 1

    # Список состояния лампочек
    lights = list()

    # Время включение света в комнате
    # Если задано время начала контроля
    if start_watching != None:
        # Проверяем тип первого элемента в списке включения - дата
        if type(els[0]) == datetime:
            # Если время контроля было раньше или в момент включения
            if els[0] >= start_watching:
                # Запоминаем время старта с момента первого включения
                start_control = els[0]
            # иначе время старта будет начало времени контроля (даже если лампочка включена)
            else:
                start_control = start_watching
        # Проверяем тип первого элемента в списке включения - кортеж
        elif type(els[0]) == tuple:
            # Если время контроля было раньше или в момент включения
            if els[0][0] >= start_watching:
                # Запоминаем время старта с момента первого включения
                start_control = els[0][0]
            # иначе время старта будет начало времени контроля (даже если лампочка включена)
            else:
                start_control = start_watching
    # Если не задано время начала контроля
    else:
        # Проверяем тип первого элемента в списке включения - дата
        if type(els[0]) == datetime:
            # Запоминаем время старта с момента первого включения
            start_control = els[0]
        # Проверяем тип первого элемента в списке включения - кортеж
        elif type(els[0]) == tuple:
            # Запоминаем время старта с момента первого включения
            start_control = els[0][0]

    print("start_control = " + str(start_control))

    # Время выключение света в комнате
    # Если задано время окончания контроля
    if end_watching != None:
        # Проверяем тип последнего элемента в списке выключения - дата
        if type(els[-1]) == datetime:
            # Если время окончания контроля было раньше или в момент выключения
            if els[-1] >= end_watching:
                # Запоминаем время финиша с момента окончания контроля
                end_control = end_watching
            # иначе время финиша будет время последнего выключения (кол-во включений = кол-ву выключений)
            else:
                end_control = els[-1]
        # Проверяем тип последнего элемента в списке выключения - кортеж
        elif type(els[-1]) == tuple:
            # Если время окончания контроля было раньше или в момент выключения
            if els[-1][0] >= end_watching:
                # Запоминаем время финиша с момента окончания контроля
                end_control = end_watching
            # иначе время финиша будет время последнего выключения (кол-во включений = кол-ву выключений)
            else:
                end_control = els[-1][0]
    # Если не задано время окончания контроля
    else:
        # Проверяем тип последнего элемента в списке выключения - дата
        if type(els[-1]) == datetime:
            # Запоминаем время финиша с момента последнего выключения
            end_control = els[-1]
        # Проверяем тип последнего элемента в списке выключения - кортеж
        elif type(els[-1]) == tuple:
            # Запоминаем время старта с момента первого включения
            end_control = els[-1][0]

    print("end_control = " + str(end_control))

    # Поиск максимального количества лампочек
    for el in els:
        if type(el) == tuple:
            if max_light < el[1]:
                max_light = el[1]

    print("Максимум лампочек = " + str(max_light))

    # Заполняем весь список состоянию лампочек как выключенные
    for i in range(0, max_light):
        lights[i] = False

    def status_lights(lights_list: list, light_index: int) -> bool:
        """
        Функция, которая меняет состояние указанной лампочки и
        проверяет состояние лампоче (включена/выключена) и выдает:
        True - если горит хотя бы одна лампочка
        False - если все лампочки погашены

        :param lights_list: переданный список лампочек
        :param light_index: индекс изменяемой лампочки
        :return: общий статус освещения комнаты
        """
        lights_list[light_index] = not lights_list[light_index]

        return True if True in lights_list else False

    # Последний статус свежения (в начале все выключено)
    last_status_lights = False

    # Проходим все временные отметки
    for el in els:
        # Определяем тип аргумента в списке
        if type(el) == datetime:
            # Меняем статусы соответствущих лампочек и проверяем последний статус освещения
            # Если свет горит, а последний статус False - свет только что загорелся
            if status_lights(lights, 0) and not last_status_lights:
                # Меняем статус на включено
                last_status_lights = True
                # Запоминаем время включения
                light_on = el
                # Проверка с end_control и start_control

            # Запоминаем поступившее время
            time = el
        elif type(el) == tuple:
            # Меняем статусы соответствущих лампочек
            lights[el[1] - 1] = not lights[el[1] - 1]
            # Запоминаем поступившее время
            time = el[0]

    def status(lights_list:list, light_index:int) -> bool:
        pass




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
