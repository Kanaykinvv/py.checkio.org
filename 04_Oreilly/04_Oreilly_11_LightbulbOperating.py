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

    # Словарь состоянием лампочек
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

    # Заполняем весь словарь состоянием лампочек как lights[номер_лампочки] = []
    # 0 - состояние
    # 1 - время включения
    # 2 - время выключения
    # 3 - заданное время работы лампочки (ее ресурс)
    # 4 - время работы лампочки
    for i in range(max_light):
        lights[i] = [False, datetime, datetime, None, datetime]

    # Заполняем остаток времени работы каждой лампочки (если задано)
    if operating != None:
        for i2 in range(max_light):
            lights[i2][3] = operating
            lights[i2][4] = operating

    print("Словарь состояний лампочек: " + str(lights))

    # Внутренняя функция проверяющая общее освещение комнаты
    def lights_room(all_lights:list)->bool:
        # Проходим по всему списку
        for lamp in range(max_light):
            # Если хоть одна лампочка освещает комнату
            if all_lights[lamp][0]:
                # Возвращаем True
                return True
        # Иначе False
        return False

    # Проходим все временные отметки
    for index in range(len(els)):

        print("Элемент списка № " + str(index))

        # Номер лампочки в текущей верменной отметке
        lamp_number = int
        # Поступившее время
        lamp_time = datetime

        # Определяем тип аргумента в списке
        if type(els[index]) == datetime:
            print("Это тип datetime: " + str(els[index]))
            lamp_number = 0
            lamp_time = els[index]
        elif type(els[index]) == tuple:
            print("Это тип tuple: " + str(els[index]))
            lamp_number = els[index][1]
            lamp_time = els[index][0]

        print("lamp_number = " + str(lamp_number))
        print("lamp_time = " + str(lamp_time))

        # Проверяем время работы лампочек при поступлении любого сигнала
        for i3 in range(max_light):
            # Если сигнал по текущей лампочки
            if i3 == lamp_number:
                # Если лампочка горела
                if lights[lamp_number][0]:

                    # Выключаем лампочку
                    lights[lamp_number][0] = False
                    # Запоминаем время выключения
                    lights[lamp_number][2] = lamp_time

                    # Проверяем выработку ее ресурса - ресурс еще есть
                    if lights[lamp_number][4] > timedelta(seconds=0):
                        # Проверяем время окончания
                        if (lights[lamp_number][1] + lights[lamp_number][4]) < lights[lamp_number][2]:
                            lights[lamp_number][2] = lights[lamp_number][1] + lights[lamp_number][4]
                        lights[lamp_number][4] -= timedelta(lights[lamp_number][2] - lights[lamp_number][1])
                        print("lights[lamp_number][4] после вычитания = " + str(lights[lamp_number][4]))
                # Если лампочка не горела
                else:
                    # Проверяем выработку ее ресурса - Если он остался или он бесконечен (не задан)
                    if (lights[lamp_number][4] > timedelta(seconds=0)) or (lights[lamp_number][3] is None):
                        # Включаем лампочку
                        lights[lamp_number][0] = True
                        # Запоминаем время включения
                        lights[lamp_number][1] = lamp_time
            # Если сигнал не под текущей лампочки
            else:
                # Если лампочка горела
                if lights[i3][0]:
                    # Проверяем выработку ее ресурса - Если он остался и задан
                    if (lights[i3][4] > timedelta(seconds=0)) and (lights[i3][3] is not None):
                        # Проверяем, сможет ли лампочка гореть до текущего момента - если не может
                        if (lamp_time - lights[i3][1]) > lights[i3][4]:
                            # Выключаем лампочку
                            lights[i3][0] = False
                            # Запоминаем время выключения
                            lights[i3][2] = lights[i3][1] + lights[i3][4]
                            # Время работы лампочки аннулируем
                            lights[i3][4] = timedelta(seconds=0)
                    # Иначе ничего, лампочка может гореть и дальше (ресурс или бесконечен или у него есть запас)
                # Если лампочка не горела горела: ничего и проверять

    # Проверяем статус освещения комнаты - Если комната не освещалась
    if lights_room(lights) and not last_status_lights:
        light_on = lamp_time

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