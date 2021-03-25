# Раз ты тут, значит ты уже решил 4 предыдущие миссии серии. Твоя функция уже может в массиве дат принимать более
# одной лампочки, чтобы определить, освещено помещение или нет. А вторым и третьим элементами можно определить - какой
# именно период мы хотим наблюдать.
#
# На 5ой миссии добавляется 4ый аргумент - время работы лампочек. По аналогии с предыдущими миссиями - если он не
# передан, значит лампа работает бесконечно.
#
# Аргумент времени работы передается как объект timedelta. Он показывает - сколько лампа может проработать во
# включенном состоянии. У нее нет остываний, а значит, если наша лампа может проработать только один час, это значит,
# что она может проработать 30 мин сейчас и 30 мин через год. Потом она сама выключится и больше не будет реагировать
# на кнопку.
#
# Нам по-прежнему надо посчитать, как долго помещение было освещено.
#
# example
#
# Input: Четыре аргумента и только первый обязательный. Первый – a list of datetime objects(вместо datetime может
# быть [datetime, int]), а второй и третий – the datetime objects. Четвертый аргумент (operating) - timedelta object -
# как долго работала лампочка.
#
# Output: Количество секунд как integer.
#
# Example:
#
# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 30),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], operating=timedelta(seconds=20)) == 40
#
# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 20), 2),
#     (datetime(2015, 1, 12, 10, 1, 40), 2),
# ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50
#
# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
# ],
# start_watching=datetime(2015, 1, 12, 10, 0, 10),
# end_watching=datetime(2015, 1, 12, 10, 0, 30),
# operating=timedelta(seconds=5)) == 10

# Предусловия:
#
# Массив нажатий на кнопку всегда отсортирован по возрастанию
# В массиве нажатий на кнопку нет повторяющихся элементов
# Количество элементов всегда четное число (это значит, что лампочка, в конце концов, будет выключена)
# Минимально возможная дата 1970-01-01
# Максимально возможная дата 9999-01-01

# Taken from mission Multiple Lightbulbs

# Taken from mission Lightbulb End Watching

# Taken from mission Lightbulb Start Watching

# Taken from mission Lightbulb Intro
#
# from datetime import datetime
# from typing import List
#
#
# def sum_light(els: List[datetime]) -> int:
#     """
#         how long the light bulb has been turned on
#     """
#     seconds = 0
#     for index in range(0, len(els) - 1, 2):
#         all_time = els[index + 1] - els[index]
#         seconds += all_time.total_seconds()
#     return seconds
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
#
# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
#     """
#         how long the light bulb has been turned on
#     """
#     seconds = 0
#
#     for index in range(0, len(els) - 1, 2):
#         if start_watching != None:
#             if start_watching < els[index]:
#                 all_time = els[index + 1] - els[index]
#                 seconds += all_time.total_seconds()
#             elif (els[index + 1] - start_watching).total_seconds() > 0:
#                 all_time = els[index + 1] - start_watching
#                 seconds += all_time.total_seconds()
#         else:
#             all_time = els[index + 1] - els[index]
#             seconds += all_time.total_seconds()
#     return seconds
#
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
#
# from datetime import datetime
# from typing import List, Optional
#
#
# def sum_light(els: List[datetime], start_watching: Optional[datetime] = None,
#               end_watching: Optional[datetime] = None) -> int:
#     """
#         how long the light bulb has been turned on
#     """
#     seconds = 0
#
#     if len(els) % 2 > 0:
#         els_1 = els[:-1]
#         els_2 = els[-1:]
#     else:
#         els_1 = els[:]
#         els_2 = None
#
#     for index in range(0, len(els_1) - 1, 2):
#         if start_watching != None:
#             if start_watching >= els_1[index + 1]:
#                 start = els_1[index + 1]
#             elif (start_watching > els_1[index]) and (start_watching < els_1[index + 1]):
#                 start = start_watching
#             else:
#                 start = els_1[index]
#         else:
#             start = els_1[index]
#
#         if end_watching != None:
#             if end_watching >= els_1[index + 1]:
#                 finish = els_1[index + 1]
#             elif (end_watching > els_1[index]) and (end_watching < els_1[index + 1]):
#                 finish = end_watching
#             else:
#                 finish = els_1[index]
#         else:
#             finish = els_1[index + 1]
#
#         all_time = finish - start
#         seconds += all_time.total_seconds()
#
#     if els_2 and len(els_2) > 0:
#         if start_watching != None:
#             start = start_watching if start_watching > els_2[0] else els_2[0]
#         else:
#             start = els_2[0]
#
#         if end_watching != None:
#             finish = end_watching if end_watching > els_2[0] else els_2[0]
#         else:
#             finish = els_2[0]
#
#         all_time = finish - start
#         seconds += all_time.total_seconds()
#
#     return seconds
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
#
# from datetime import datetime
# from typing import List, Optional, Union, Tuple
#
#
# def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
#               start_watching: Optional[datetime] = None,
#               end_watching: Optional[datetime] = None) -> int:
#     # Количество секунд освещение комнаты
#     seconds = 0
#
#     # Максимальное количество лампочек (по-умолчанию 1)
#     max_light = 1
#
#     # Список состояния лампочек
#     lights = list()
#
#     # Границы контроля времени для замера - начало
#     start_control = ""
#     # Границы контроля времени для замера - конец
#     end_control = ""
#
#     # Последний статус свечения (в начале все выключено)
#     last_status_lights = False
#
#     # Время начала освещения комнаты
#     light_on = ""
#
#     # Время конца освещения комнаты
#     light_off = ""
#
#     # Время включение света в комнате
#     # Если задано время начала контроля
#     if start_watching != None:
#         # Проверяем тип первого элемента в списке включения - дата
#         if type(els[0]) == datetime:
#             # Если время контроля было раньше или в момент включения
#             if els[0] >= start_watching:
#                 # Запоминаем время старта с момента первого включения
#                 start_control = els[0]
#             # иначе время старта будет начало времени контроля (даже если лампочка включена)
#             else:
#                 start_control = start_watching
#         # Проверяем тип первого элемента в списке включения - кортеж
#         elif type(els[0]) == tuple:
#             # Если время контроля было раньше или в момент включения
#             if els[0][0] >= start_watching:
#                 # Запоминаем время старта с момента первого включения
#                 start_control = els[0][0]
#             # иначе время старта будет начало времени контроля (даже если лампочка включена)
#             else:
#                 start_control = start_watching
#     # Если не задано время начала контроля
#     else:
#         # Проверяем тип первого элемента в списке включения - дата
#         if type(els[0]) == datetime:
#             # Запоминаем время старта с момента первого включения
#             start_control = els[0]
#         # Проверяем тип первого элемента в списке включения - кортеж
#         elif type(els[0]) == tuple:
#             # Запоминаем время старта с момента первого включения
#             start_control = els[0][0]
#
#     # Время выключение света в комнате
#     # Если задано время окончания контроля
#     if end_watching != None:
#         end_control = end_watching
#
#     else:
#         # Проверяем тип последнего элемента в списке выключения - дата
#         if type(els[-1]) == datetime:
#             # Запоминаем время финиша с момента последнего выключения
#             end_control = els[-1]
#         # Проверяем тип последнего элемента в списке выключения - кортеж
#         elif type(els[-1]) == tuple:
#             # Запоминаем время старта с момента первого выключения
#             end_control = els[-1][0]
#
#     # Поиск максимального количества лампочек
#     for el in els:
#         if type(el) == tuple:
#             if max_light < el[1]:
#                 max_light = el[1]
#
#     # Заполняем весь список состоянию лампочек как выключенные
#     for i in range(max_light):
#         lights.append(False)
#
#     # Проходим все временные отметки
#     for index in range(len(els)):
#
#         # Определяем тип аргумента в списке
#         if type(els[index]) == datetime:
#
#             # Меняем статусы соответствущих лампочек и проверяем освещение
#             lights[0] = not lights[0]
#             status_lights = True if True in lights else False
#
#             # Если свет горит, а последний статус False - следовательно освещение в комнате включилось
#             if status_lights and not last_status_lights:
#
#                 # Меняем статус на включено
#                 last_status_lights = True
#                 # Запоминаем время включения
#                 if els[index] <= start_control:
#                     light_on = start_control
#                 elif (els[index] > start_control) and (els[index] < end_control):
#                     light_on = els[index]
#                 else:
#                     light_on = end_control
#
#             # Если свет погас, а последний статус True - следовательно освещение в комнате выключилось
#             if not status_lights and last_status_lights:
#
#                 # Меняем статус на выключено
#                 last_status_lights = False
#                 # Запоминаем время выключения
#                 if els[index] >= end_control:
#                     light_off = end_control
#                 elif (els[index] > start_control) and (els[index] < end_control):
#                     light_off = els[index]
#                 else:
#                     light_off = light_on
#
#                 # Считаем количество времени освещения
#                 seconds += (light_off - light_on).total_seconds()
#
#             # Если свет горит, а элемент последний, вычисляем время освещения до границы наблюдения
#             if status_lights and (index == len(els) - 1):
#                 # Считаем количество времени освещения
#                 seconds += (end_control - light_on).total_seconds()
#
#
#         elif type(els[index]) == tuple:
#
#             # Меняем статусы соответствущих лампочек и проверяем освещение
#             lights[els[index][1] - 1] = not lights[els[index][1] - 1]
#             status_lights = True if True in lights else False
#
#             # Если свет горит, а последний статус False - следовательно освещение в комнате включилось
#             if status_lights and not last_status_lights:
#
#                 # Меняем статус на включено
#                 last_status_lights = True
#                 # Запоминаем время включения
#                 if els[index][0] <= start_control:
#                     light_on = start_control
#                 elif (els[index][0] > start_control) and (els[index][0] < end_control):
#                     light_on = els[index][0]
#                 else:
#                     light_on = end_control
#
#             # Если свет погас, а последний статус True - следовательно освещение в комнате выключилось
#             if not status_lights and last_status_lights:
#
#                 # Меняем статус на выключено
#                 last_status_lights = False
#                 # Запоминаем время выключения
#                 if els[index][0] >= end_control:
#                     light_off = end_control
#                 elif (els[index][0] > start_control) and (els[index][0] < end_control):
#                     light_off = els[index][0]
#
#                 # Считаем количество времени освещения
#                 seconds += (light_off - light_on).total_seconds()
#
#             # Если свет горит, а элемент последний, вычисляем время освещения до границы наблюдения
#             if status_lights and (index == len(els) - 1):
#                 # Считаем количество времени освещения
#                 seconds += (end_control - light_on).total_seconds()
#
#     return seconds
#
#
# if __name__ == '__main__':
#     print("Example:")
#
#     print(sum_light(els=[
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], start_watching=datetime(2015, 1, 12, 10, 0, 0), end_watching=datetime(2015, 1, 12, 10, 1, 0)))
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ]) == 60
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 11, 0, 0), 2),
#         (datetime(2015, 1, 12, 11, 1, 0), 2),
#     ]) == 70
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ]) == 30
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ]) == 40
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#         (datetime(2015, 1, 12, 10, 1, 0), 3),
#         (datetime(2015, 1, 12, 10, 1, 20), 3),
#     ]) == 60
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ], datetime(2015, 1, 12, 10, 0, 50)) == 10
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 30)) == 20
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 20)) == 30
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 10)) == 30
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 50)) == 0
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 30)) == 20
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 20)) == 30
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#         (datetime(2015, 1, 12, 10, 1, 20), 2),
#         (datetime(2015, 1, 12, 10, 1, 40), 2),
#     ], datetime(2015, 1, 12, 10, 0, 20)) == 50
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ], datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#     ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30)) == 30
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         datetime(2015, 1, 12, 10, 0, 40),
#         (datetime(2015, 1, 12, 10, 0, 50), 2),
#     ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#     ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10
#
#     assert sum_light([
#         (datetime(2015, 1, 12, 10, 0, 10), 3),
#         datetime(2015, 1, 12, 10, 0, 20),
#         (datetime(2015, 1, 12, 10, 0, 30), 3),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#     ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20
#
#     assert sum_light(els=[
#         (datetime(2015, 1, 11, 0, 0, 0), 3),
#         datetime(2015, 1, 12, 0, 0, 0),
#         (datetime(2015, 1, 13, 0, 0, 0), 3),
#         (datetime(2015, 1, 13, 0, 0, 0), 2),
#         datetime(2015, 1, 14, 0, 0, 0),
#         (datetime(2015, 1, 15, 0, 0, 0), 2),
#     ], start_watching=datetime(2015, 1, 10, 0, 0, 0), end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600
#
#     print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")

from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
              start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None,
              operating: Optional[timedelta] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    # Количество секунд освещение комнаты
    seconds = 0

    # Максимальное количество лампочек (по-умолчанию 1)
    max_light = 1

    # Границы контроля времени для замера - начало
    start_control = ""
    # Границы контроля времени для замера - конец
    end_control = ""

    # Последний статус свечения (в начале все выключено)
    last_status_lights = False

    # Время начала освещения комнаты
    light_on = ""

    # Время конца освещения комнаты
    light_off = ""

    # =================================Остаточное время работы лампочек
    lights = dict()


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
        end_control = end_watching

    else:
        # Проверяем тип последнего элемента в списке выключения - дата
        if type(els[-1]) == datetime:
            # Запоминаем время финиша с момента последнего выключения
            end_control = els[-1]
        # Проверяем тип последнего элемента в списке выключения - кортеж
        elif type(els[-1]) == tuple:
            # Запоминаем время старта с момента первого выключения
            end_control = els[-1][0]

    print("end_control = " + str(end_control))

    # Поиск максимального количества лампочек
    for el in els:
        if type(el) == tuple:
            if max_light < el[1]:
                max_light = el[1]

    print("Максимум лампочек = " + str(max_light))

    # Заполняем весь словарь состоянием лампочек как list_lights[номер_лампочки] = []
    # 0 - состояние
    # 1 - время включения
    # 2 - время выключения
    # 3 - остаточное время
    # 4 - время работы лампочки
    for i in range(max_light):
        # lights.append(False)
        lights[i] = [False, datetime, datetime, None, 0]
        # print("Заполнение списка light[" + str(i) + "] = " + str(lights[i]))

    # Заполняем остаток времени работы каждой лампочки (если задано)
    if operating != None:
        for i2 in range(max_light):
            lights[i2][3] = operating

    print("Словарь состояний лампочек: " + str(lights))

    # Проходим все временные отметки
    for index in range(len(els)):
        print("Элемент списка № " + str(index))

        # Определяем тип аргумента в списке
        if type(els[index]) == datetime:
            print("Это тип datetime: " + str(els[index]))
            # Проверяем горел ли свет
            if lights[0][0]:
                # Меняем состояние
                lights[0][0] = not lights[0][0]
                lights[0][4] += (lights[0][2] - lights[0][1])


        elif type(els[index]) == tuple:
            print("Это тип tuple: " + str(els[index]))
            # Меняем статусы соответствущих лампочек и проверяем освещение
            lights[index[1]][0] = not lights[index[1]][0]


    print("Количество секунд работы = " + str(seconds))
    return seconds


if __name__ == '__main__':
    print("Example:")

    print(sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ],
        start_watching=datetime(2015, 1, 12, 10, 0, 10),
        end_watching=datetime(2015, 1, 12, 10, 0, 30),
        operating=timedelta(seconds=5)))
    #
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
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 10),
    # ], operating=timedelta(seconds=100)) == 10
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 10),
    # ], operating=timedelta(seconds=5)) == 5
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 10),
    #     (datetime(2015, 1, 12, 10, 0, 0), 2),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], operating=timedelta(seconds=100)) == 60
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 30),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], operating=timedelta(seconds=100)) == 60
    #
    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 30),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], operating=timedelta(seconds=20)) == 40
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
    # ], operating=timedelta(seconds=10)) == 30
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
    # ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50
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
    # ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=10)) == 20
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    #     operating=timedelta(seconds=20)) == 20
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    #     operating=timedelta(seconds=10)) == 20
    #
    # assert sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
    #     operating=timedelta(seconds=5)) == 10
    #
    # print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")