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
        lights[i] = [False, datetime, datetime, None, None]

    # Заполняем остаток времени работы каждой лампочки (если задано)
    if operating != None:
        print("Выработка для лампочек задана = " + str(operating))
        for i2 in range(max_light):
            lights[i2][3] = operating
            lights[i2][4] = operating
    else:
        print("Выработка для лампочек не задана")
        for i2 in range(max_light):
            lights[i2][4] = timedelta(seconds=0)

    print("Словарь состояний лампочек: ")
    for print_lamp in range(max_light):
        print(str(print_lamp) + " : " + str(lights[print_lamp]))

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

        print("================= Временные отметка № " + str(index + 1) + " : " + str(els[index]) + "=================")

        # Номер лампочки в текущей верменной отметке
        lamp_number = int
        # Поступившее время
        lamp_time = datetime

        # Определяем тип аргумента в списке
        print("00 - Определяем тип аргумента в списке...")
        if type(els[index]) == datetime:
            print("01 - Это тип datetime: " + str(els[index]))
            lamp_number = 0
            lamp_time = els[index]
        elif type(els[index]) == tuple:
            print("02 - Это тип tuple: " + str(els[index]))
            lamp_number = els[index][1] - 1
            lamp_time = els[index][0]

        print("lamp_number = " + str(lamp_number))
        print("lamp_time = " + str(lamp_time))

        # Проверяем время работы лампочек при поступлении любого сигнала
        print("03 - Проверяем время работы лампочек при поступлении любого сигнала...")
        for i3 in range(max_light):
            print("04 - =========== Проверка всех лампочек (№" + str(i3) + ") ===========")
            # Если сигнал по текущей лампочки
            if i3 == lamp_number:
                print("05 - Cигнал по текущей лампочке i3 == lamp_number == " + str(i3))
                # Если лампочка горела
                if lights[lamp_number][0]:
                    print("06 - Лампочка #" + str(lamp_number) + " горела: " + str(lights[lamp_number][0]))
                    # Выключаем лампочку
                    lights[lamp_number][0] = False
                    print("07 - Выключаем лампочку: lights[lamp_number][0] = " + str(lights[lamp_number][0]))
                    # Запоминаем время выключения
                    lights[lamp_number][2] = lamp_time
                    print("08 - Запоминаем время выключения: lights[lamp_number][2] = " + str(lights[lamp_number][2]))

                    # Проверяем выработку ее ресурса - ресурс еще есть
                    print("09 - Проверяем выработку ее ресурса...")
                    print("10 - lights[lamp_number][3] = " + str(lights[lamp_number][3]))
                    print("11 - lights[lamp_number][4] = " + str(lights[lamp_number][4]))
                    if lights[lamp_number][4] > timedelta(seconds=0):
                        print("12 - Проверяем выработку ее ресурса - ресурс еще есть: lights[lamp_number][4] = " + str(lights[lamp_number][4]))
                        # Проверяем время окончания
                        print("13 - Проверяем время окончания")
                        if (lights[lamp_number][1] + lights[lamp_number][4]) < lights[lamp_number][2]:
                            lights[lamp_number][2] = lights[lamp_number][1] + lights[lamp_number][4]
                            print("14 - Меняем время окончания lights[lamp_number][2] = " + str(lights[lamp_number][2]))
                            lamp_time = lights[lamp_number][2]
                        print("15 - Вычитаем наработку...")
                        lights[lamp_number][4] = lights[lamp_number][4] - (lights[lamp_number][2] - lights[lamp_number][1])
                        print("16 - lights[lamp_number][4] после вычитания = " + str(lights[lamp_number][4]))
                # Если лампочка не горела
                else:
                    print("17 - Лампочка #" + str(lamp_number) + " НЕ горела: " + str(lights[lamp_number][0]))
                    # Проверяем выработку ее ресурса - Если он остался или он бесконечен (не задан)
                    print("18 - Проверяем выработку ее ресурса...")
                    print("19 - lights[lamp_number][3] = " + str(lights[lamp_number][3]))
                    print("20 - lights[lamp_number][4] = " + str(lights[lamp_number][4]))
                    if (lights[lamp_number][4] > timedelta(seconds=0)) or (lights[lamp_number][3] is None):
                        print("21 - Ресурс есть или он бесконечен")
                        # Включаем лампочку
                        lights[lamp_number][0] = True
                        print("22 - Включаем лампочку lights[lamp_number][0] = " + str(lights[lamp_number][0]))
                        # Запоминаем время включения
                        lights[lamp_number][1] = lamp_time
                        print("23 - Запоминаем время включения lights[lamp_number][1] = " + str(lights[lamp_number][1]))
            # Если сигнал не под текущей лампочки
            else:
                print("24 - Cигнал НЕ по текущей лампочке i3 != lamp_number. Лампочка = " + str(i3))
                # Если лампочка горела
                if lights[i3][0]:
                    print("25 - Лампочка горела lights[" + str(i3) + "][0] = " + str(lights[i3][0]))
                    # Проверяем выработку ее ресурса - Если он остался и задан
                    print("26 - Проверяем выработку ее ресурса...")
                    print("27 - lights[lamp_number][3] = " + str(lights[i3][3]))
                    print("28 - lights[lamp_number][4] = " + str(lights[i3][4]))
                    if (lights[i3][4] > timedelta(seconds=0)) and (lights[i3][3] is not None):
                        print("29 - Ресурс остался и задан...")
                        # Проверяем, сможет ли лампочка гореть до текущего момента - если не может
                        if (lamp_time - lights[i3][1]) > lights[i3][4]:
                            print("30 - Лампочка не может гореть до текущего момента...")
                            # Выключаем лампочку
                            lights[i3][0] = False
                            print("31 - Выключаем лампочку lights[i3][0] = " + str(lights[i3][0]))
                            # Запоминаем время выключения
                            lights[i3][2] = lights[i3][1] + lights[i3][4]
                            print("32 - Запоминаем время выключения lights[i3][2] = " + str(lights[i3][2]))
                            # Время работы лампочки аннулируем
                            lights[i3][4] = timedelta(seconds=0)
                            print("33 - Время работы лампочки аннулируем lights[i3][4] = " + str(lights[i3][4]))

                    else:
                        # Иначе ничего, лампочка может гореть и дальше (ресурс или бесконечен или у него есть запас)
                        print("34 - Лампочка может гореть и дальше (ресурс или бесконечен или у него есть запас)")
                else:
                    # Если лампочка не горела: ничего и проверять
                    print("35 - Лампочка не горела: ничего и проверять")

        # Проверяем статус освещения комнаты - Если комната не освещалась и начала освещаться
        print("36 - Проверяем статус освещения комнаты...")
        if lights_room(lights) and not last_status_lights:
            print("37 - Комната не освещалась и начала освещаться")
            # Запоминаем время включения
            light_on = lamp_time
            print("38 - Запоминаем время включения light_on = " + str(light_on))
            # Меняем последний статус свечения
            last_status_lights = True
            print("39 - Меняем последний статус свечения last_status_lights = " + str(last_status_lights))
        # Проверяем статус освещения комнаты - Если комната освещалась и перестала освещаться
        elif (not lights_room(lights) and last_status_lights) or (lights_room(lights) and (index == len(els) - 1)):
            if not lights_room(lights) and last_status_lights:
                print("40 - Комната освещалась и перестала освещаться")
            elif lights_room(lights) and (index == len(els) - 1):
                print("40 - Комната освещалась и поступил последний временной сигнал")
            # Запоминаем время выключения
            light_off = lamp_time
            print("41 - Запоминаем время выключения light_off = " + str(light_off))
            # Меняем последний статус свечения
            last_status_lights = False
            print("42 - Меняем последний статус свечения last_status_lights = " + str(last_status_lights))

            print("43 - Проверяем границы start_control...")
            if light_on <= start_control:
                print("44 - light_on (" + str(light_on) + ") <= start_control (" + str(start_control) + ")")
                print("45 - light_on = start_control")
                light_on = start_control
            elif light_on >= end_control:
                print("46 - light_on (" + str(light_on) + ") >= end_control (" + str(end_control) + ")")
                print("47 - light_on = end_control")
                light_on = end_control
            else:
                print("48 - С light_on все хорошо")

            print("49 - Проверяем границы end_control...")
            if light_off >= end_control:
                print("50 - light_off (" + str(light_off) + ") >= end_control (" + str(end_control) + ")")
                print("51 - light_off = end_control")
                light_off = end_control
            elif lights_room(lights) and (index == len(els) - 1):
                print("52 - Последний временной сигнал, комната освещена, поэтому light_off = end_control")
                light_off = end_control

            print("53 - Производим подсчет seconds...")
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
            print("light_on = " + str(light_on))
            print("light_off = " + str(light_off))
            print("seconds = " + str(seconds))
            print("-------------------------------")
            print("seconds += (light_off - light_on)")
            seconds += (light_off - light_on).total_seconds()
            print("seconds = " + str(seconds))
            print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
        else:
            print("54 - Комната продолжает освещаться и " + str(index) + " не последний сигнал")

    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
    print("55 - Количество секунд работы = " + str(seconds))
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")

    return seconds

# В процессе перебора временных отметок необходимо сформировать новый список с временными отметками,
# который будет включать новые отметки по закончившими работать лампочками по окончании их ресурса
# И второе - необходимо проверять входной список временных отметок на сортировку, или проводить сортировку нового списка

if __name__ == '__main__':
    print("Example:")

    # print(sum_light([
    #     (datetime(2015, 1, 12, 10, 0, 10), 3),
    #     datetime(2015, 1, 12, 10, 0, 20),
    #     (datetime(2015, 1, 12, 10, 0, 30), 3),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    # ],
    #     start_watching=datetime(2015, 1, 12, 10, 0, 10),
    #     end_watching=datetime(2015, 1, 12, 10, 0, 30),
    #     operating=timedelta(seconds=5)))
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

# Массив не отсортирован, при  сортировке все хорошо, реализовать предварительную сортировку
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         (datetime(2015, 1, 12, 10, 0, 0), 2),
#         datetime(2015, 1, 12, 10, 0, 10),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ], operating=timedelta(seconds=100)) == 60
#
#     assert sum_light([
#         datetime(2015, 1, 12, 10, 0, 0),
#         datetime(2015, 1, 12, 10, 0, 30),
#         (datetime(2015, 1, 12, 10, 0, 30), 2),
#         (datetime(2015, 1, 12, 10, 1, 0), 2),
#     ], operating=timedelta(seconds=100)) == 60

    # assert sum_light([
    #     datetime(2015, 1, 12, 10, 0, 0),
    #     datetime(2015, 1, 12, 10, 0, 30),
    #     (datetime(2015, 1, 12, 10, 0, 30), 2),
    #     (datetime(2015, 1, 12, 10, 1, 0), 2),
    # ], operating=timedelta(seconds=20)) == 40

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
    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
        operating=timedelta(seconds=5)) == 10
    #
    # print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")