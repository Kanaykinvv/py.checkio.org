# Усложнением 6ой миссии серии является то, что теперь для освещения помещения может понадобиться более одной лампочки.
# И это 5й аргумент функции - сколько лампочек нужно для освещения помещения.
#
# Например, если для освещения помещения нужно 3 лампочки, то мы не засчитываем то время, когда лампочек
# было всего 2 или только одна. Если последний аргумент функции не передан, значит достаточно одной лампочки
# для освещения помещения.
#
# Задача все та же - узнать сколько времени помещение было освещено (в этой задаче можно сказать - достаточно освещено).
#
# Input: Пять аргументов и только первый обязательный. Первый – a list of datetime objects(вместо datetime может быть
# [datetime, int]), а второй и третий – the datetime objects. Четвертый аргумент (operating) - timedelta object -
# как долго работала лампочка. Пятый аргумент - положительный int
#
# Output: Количество секунд как integer.

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=2) == 20
#
# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=3) == 0
#
# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 0, 50), 3),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=3) == 10

# Предусловия:
#
# Массив нажатий на кнопку всегда отсортирован по возрастанию.
# В массиве нажатий на кнопку нет повторяющихся элементов.
# Минимально возможная дата 1970-01-01.
# Максимально возможная дата 9999-12-31.
# req > 0

from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
              start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None,
              operating: Optional[timedelta] = None,
              req: Optional[int] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    # -/-/-/-/-/-/-/-/-/-/-/-/-/
    #       Переменные
    # -/-/-/-/-/-/-/-/-/-/-/-/-/
    # Количество секунд освещение комнаты
    seconds = 0
    # Максимальное количество лампочек (по-умолчанию 1)
    max_light = 1
    # Необходимое количество лампочек для освещения комнаты (по-умолчанию 1)
    count_light = 1
    # Границы контроля времени для замера - начало
    start_control = ""
    # Границы контроля времени для замера - конец
    end_control = ""
    # Словарь состоянием лампочек
    lights = dict()
    # Внутренний параметр вывода подсказок (лога)
    show_hint = False

    # -/-/-/-/-/-/-/-/-/-/-/-/-/
    #       Внутренние методы
    # -/-/-/-/-/-/-/-/-/-/-/-/-/

    def find_count_light(def_req: Optional[int] = None) -> int:
        """
        Определение необходимого числа лампочек для освещения комнаты
        :param def_req: Заданный параметр количества лампочек
        :return: Необходимое количество лампочек
        """
        # Если задано количество необходимых лампочек
        if def_req != None:
            # Выдаем это значение
            return def_req
        else:
            # Иначе необходима 1 лампочка
            return 1

    # Определение границы контроля времени - начало контроля (поиск start_control)
    def find_start_control(def_els: List[Tuple[datetime, int]],
                           def_start_watching: Optional[datetime] = None) -> datetime:
        """
        Определение границы контроля времени - начало контроля (поиск start_control)
        :param def_els: - отсортированный список временных отметок (с указанными номерами лампочек)
        :param def_start_watching: - опциональный параметр времени начала контроля
        :return: - время начала контроля (для переменной start_control)
        """
        # Если задано время начала контроля
        if def_start_watching != None:
            # Если время контроля было раньше или в момент включения
            if def_els[0][0] >= def_start_watching:
                # Выдаем время старта с момента первого включения
                return def_els[0][0]
            # иначе время старта будет начало времени контроля (даже если лампочка включена)
            else:
                return def_start_watching
        # Если не задано время начала контроля
        else:
            # Выдаем время старта с момента первого сигнала
            return def_els[0][0]

    # Определение границы контроля времени - окончания контроля (поиск end_control)
    def find_end_control(def_els: List[Tuple[datetime, int]],
                         def_end_watching: Optional[datetime] = None) -> datetime:
        """
        Определение границы контроля времени - окончания контроля (поиск end_control)
        :param def_els: - отсортированный список временных отметок (с указанными номерами лампочек)
        :param def_end_watching: - опциональный параметр времени окончания контроля
        :return: - время кончания контроля (для переменной end_control)
        """
        # Если задано время окончания контроля
        if def_end_watching != None:
            # Выдаем его
            return def_end_watching
        else:
            # Выдаем время с момента последнего сигналв
            return def_els[-1][0]

    # Поиск максимального количества лампочек в исходном списке
    def find_max_light(def_els: List[Union[datetime, Tuple[datetime, int]]]) -> int:
        """
        Поиск максимального количества лампочек в исходном списке
        :param def_els:  - исходный список (оригинальный, не сортированный, без дополнительных временных отметок)
        :return: - максимальное количество лампочек (для переменной max_light)
        """
        # Локальная переменная максимального количества лампочек (по умолчанию 1)
        def_max_light = 1

        # Перебор всего списка
        for el in def_els:
            # Если элемент это кортеж, следовательно у него есть номер лампочки (по условию)
            if type(el) == tuple:
                # Сверяем указанную лампочку в кортеже с запомненной (в кортеже лампочки идут с 2-й)
                if def_max_light < el[1]:
                    # Если запомненная лампочка меньше текущей, запоминаем текущую как максимальную
                    def_max_light = el[1]

        # После перебора возвращаем число лампочек
        return def_max_light

        if show_hint: print("Максимум лампочек = " + str(max_light))

    # Заполнение списка
    def fill_lights(def_max_light: int) -> list():
        """
        Создает и заполняет список списков лампочек:
        Заполняем весь словарь состоянием лампочек как lights[номер_лампочки] = []
            0 - состояние
            1 - время включения
            2 - время выключения
            3 - заданное время работы лампочки (ее ресурс)
            4 - время работы лампочки
        :return: - возвращает заполненный чистый список
        """

        # Результирующий список
        result = dict()

        # Заполняем список исходными списками по количеству лампочек
        for i in range(def_max_light):
            result[i] = [False, datetime, datetime, None, None]

        # Заполняем остаток времени работы каждой лампочки (если задано)
        if operating != None:
            for i2 in range(def_max_light):
                result[i2][3] = operating
                result[i2][4] = operating
        else:
            for i2 in range(def_max_light):
                result[i2][4] = timedelta(seconds=0)

        return result

    # Проверка освещения комнаты
    def lights_room(all_lights: list, def_req: int) -> bool:
        """
        Проверка освещения комнаты по количеству включенных лампочек
        :param all_lights: список списков лампочек
        :param def_req: количество необходимых включенных лампочек, чтобы комната считалась освещенной
        :return: результат освещения (True) комнаты, или темноты в ней (False)
        """
        current_on_lights = 0
        # Проходим по всему списку
        for lamp in range(len(all_lights)):
            # Если лампочка освещает включена
            if all_lights[lamp][0]:
                # Увеличиваем счетчик включенных лампочек
                current_on_lights += 1
        return True if current_on_lights >= def_req else False

    # Создание полного списка всех временных сигналов
    # (создание новых сигналов по отработке)
    def all_signal() -> List[Tuple[datetime, int]]:
        """
        Создание полного списка всех временных сигналов
        (создание и добавление новых сигналов по отработке)
        :return: - список всех сигналов и номеров лампочек
        """
        result = list()

        if show_hint: print("Создание полного списка всех временных сигналов")

        # Проходим все временные отметки
        for index in range(len(els)):
            if show_hint: print("Проходим все временные отметки в исходном списке (els): index = " + str(index))
            # Номер лампочки в текущей верменной отметке
            lamp_number = int
            # Поступившее время
            lamp_time = datetime

            # Определяем тип аргумента в списке
            if type(els[index]) == datetime:
                if show_hint: print("type(els[index]) == datetime")
                lamp_number = 0
                lamp_time = els[index]
            elif type(els[index]) == tuple:
                if show_hint: print("type(els[index]) == tuple")
                lamp_number = els[index][1] - 1
                lamp_time = els[index][0]

            if show_hint: print("lamp_number = " + str(lamp_number))
            if show_hint: print("lamp_time = " + str(lamp_time))

            if show_hint: print("# Проверяем время работы всех лампочек при поступлении любого сигнала")

            # Проверяем время работы лампочек при поступлении любого сигнала
            for i3 in range(max_light):
                if show_hint: print("-"*50)
                if show_hint: print("# Лампочка №" + str(i3) + "/" + str(max_light-1))
                # Если сигнал по текущей лампочки
                if i3 == lamp_number:
                    if show_hint: print("# Сигнал по текущей лампочке (lamp_number = перебору)")
                    # Если лампочка горела
                    if lights[lamp_number][0]:
                        if show_hint: print("# Лампочка горела ")
                        # Выключаем лампочку
                        lights[lamp_number][0] = False
                        if show_hint: print("# Выключаем лампочку lights[" + str(lamp_number) + "][0] = " + str(lights[lamp_number][0]))
                        # Запоминаем время выключения
                        lights[lamp_number][2] = lamp_time
                        if show_hint: print("# Запоминаем время выключения lights[" + str(lamp_number) + "][2] = " + str(lights[lamp_number][2]))
                        # Проверяем выработку ее ресурса - ресурс еще есть
                        if lights[lamp_number][4] > timedelta(seconds=0):
                            if show_hint: print("# Проверяем выработку ее ресурса - ресурс еще есть ")
                            # Проверяем время окончания
                            if (lights[lamp_number][1] + lights[lamp_number][4]) < lights[lamp_number][2]:
                                if show_hint: print("# Проверяем время окончания - окончание по выработке")
                                lights[lamp_number][2] = lights[lamp_number][1] + lights[lamp_number][4]
                            if show_hint: print("Записываем выработку")
                            lights[lamp_number][4] = lights[lamp_number][4] - (
                                        lights[lamp_number][2] - lights[lamp_number][1])
                        # Проверяем отсутствие выработки ресурса
                        elif lights[lamp_number][3] is None:
                            if show_hint: print("# Проверяем выработку ее ресурса - ресурс НЕ задан ")
                        result.append((lights[lamp_number][2], lamp_number))
                        if show_hint: print("result.append((" + str(lamp_time) + ", " + str(lamp_number) + ")) ")
                    # Если лампочка не горела
                    else:
                        if show_hint: print("# Лампочка не горела ")
                        # Проверяем выработку ее ресурса - Если он остался или он бесконечен (не задан)
                        if (lights[lamp_number][4] > timedelta(seconds=0)) or (lights[lamp_number][3] is None):
                            if show_hint: print("# Проверяем выработку ее ресурса - Если он остался или он бесконечен (не задан)")
                            # Включаем лампочку
                            lights[lamp_number][0] = True
                            if show_hint: print("# Включаем лампочку lights[" + str(lamp_number) + "][0] = " + str(lights[lamp_number][0]))
                            # Запоминаем время включения
                            lights[lamp_number][1] = lamp_time
                            if show_hint: print("# Запоминаем время включения lights[" + str(lamp_number) + "][1] = " + str(lights[lamp_number][1]))
                            result.append((lamp_time, lamp_number))
                            if show_hint: print("result.append((" + str(lamp_time) + ", " + str(lamp_number) +")) ")
                # Если сигнал не под текущей лампочки
                else:
                    if show_hint: print("# Сигнал НЕ по текущей лампочке (lamp_number != перебору)")
                    # Если лампочка горела
                    if lights[i3][0]:
                        if show_hint: print("# Лампочка горела")
                        # Проверяем выработку ее ресурса - Если он остался и задан
                        if (lights[i3][4] > timedelta(seconds=0)) and (lights[i3][3] is not None):
                            if show_hint: print("# Ресурс задан и больше 0")
                            # Проверяем, сможет ли лампочка гореть до текущего момента - если не может
                            if (lamp_time - lights[i3][1]) > lights[i3][4]:
                                if show_hint: print("# Лампочка НЕ может гореть до текущего момента")
                                # Выключаем лампочку
                                lights[i3][0] = False
                                if show_hint: print("# Выключаем лампочку lights[" + str(i3) + "][0] = " + str(lights[i3][0]))
                                # Запоминаем время выключения
                                lights[i3][2] = lights[i3][1] + lights[i3][4]
                                if show_hint: print("# Запоминаем время выключения lights[" + str(i3) + "][2] = " + str(lights[i3][2]))
                                result.append((lights[i3][2], i3))
                                if show_hint: print("result.append((" + str(lights[i3][2]) + ", " + str(i3) +")) ")
                                # Время работы лампочки аннулируем
                                lights[i3][4] = timedelta(seconds=0)
                                if show_hint: print("# Время работы лампочки аннулируем lights[" + str(i3) + "][4] = " + str(lights[i3][4]))
                            else:
                                if show_hint: print("# Лампочка может гореть до текущего момента")
                        else:
                            if show_hint: print("# Ресурс не задан (None)")
                    else:
                        if show_hint: print("# Если лампочка НЕ горела - ничего не делаем")

                if show_hint: print("-" * 50)
        return result

    # Сортировка входящего списка временных сигналов по возрастанию времени методом пузырька
    # (т.к. в тестах обнаружено, что не выполняется условие возрастания временных отметок)
    def sort_els(els_in: List[Tuple[datetime, int]]) -> List[Tuple[datetime, int]]:
        """
        Сортировка входящего списка временных сигналов по возрастанию времени методом пузырька
        (т.к. в тестах обнаружено, что не выполняется условие возрастания временных отметок)
        :param els_in: - входящий список временных сигналов
        :return: - отсортированный списоквременных сигналов по возрастанию времени
        """
        # Количество проходов равно количеству элементов
        for run in range(len(els_in)-1):
            for index_el in range(len(els_in) - 1):
                if els_in[index_el][0] > els_in[index_el+1][0]:
                    els_in[index_el], els_in[index_el+1] = els_in[index_el+1], els_in[index_el]
        return els_in

    # Проход по всем временным отметкам с включением\выключением лампочек и подсчетом времени освещения
    def count_seconds(end_els: List[Tuple[datetime, int]], def_lights: dict, def_count_light: int) -> int:
        """
        # Проход по всем временным отметкам с включением\выключением лампочек и подсчетом времени освещения
        :return: - количество секунд освещения комнаты
        """
        # Количество секунд освещения комнаты
        result = 0
        # Время начала освещения комнаты
        light_on = ""
        # Время конца освещения комнаты
        light_off = ""
        # Последний статус свечения (в начале все выключено)
        last_status_lights = False


        if show_hint: print("===================================")
        if show_hint: print("--------- count_seconds ---------")
        if show_hint: print("===================================")
        if show_hint: print("Проходим все временные отметки, всего отметок " + str(len(end_els)))
        # Проходим все временные отметки
        for index in range(len(end_els)):

            if show_hint: print("Временная отметка № " + str(index + 1))
            if show_hint: print("Элемент списка : " + str(end_els[index]))

            # Номер лампочки в текущей верменной отметке
            lamp_number = end_els[index][1]
            # Поступившее время
            lamp_time = end_els[index][0]

            if show_hint: print("lamp_number = " + str(lamp_number))
            if show_hint: print("lamp_time = " + str(lamp_time))

            # Если лампочка горела
            if def_lights[lamp_number][0]:
                # Выключаем лампочку
                def_lights[lamp_number][0] = False
                if show_hint: print("Лампочка горела - > Выключаем лампочку")
            else:
                # Включаем лампочку
                def_lights[lamp_number][0] = True
                if show_hint: print("Лампочка не горела - > Включаем лампочку")

            if show_hint: print(def_lights[lamp_number])

            # Если комната не освещалась и начала освещаться
            if lights_room(def_lights, def_count_light) and not last_status_lights:
                # Запоминаем время включения
                light_on = lamp_time
                # Меняем последний статус свечения
                last_status_lights = True
                if show_hint: print("Комната не освещалась и начала освещаться")
                if show_hint: print("light_on = lamp_time = " + str(lamp_time))
                if show_hint: print("last_status_lights = True")

                # --------------------------
                # Если комната освещается и это последний временной элемент
                if index == len(end_els) - 1:
                    if show_hint: print("Комната освещается и это последний временной элемент")
                    if show_hint: print("-" * 50)

                    # Если время начала освещения комнаты раньше, чем время начала мониторинга
                    if light_on <= start_control:
                        # Время начала освещения принимаем за время начала мониторинга
                        light_on = start_control
                        if show_hint: print(
                            "Время начала освещения комнаты раньше, чем время начала мониторинга: light_on = start_control = " + str(
                                start_control))
                    # Если время начала освещения комнаты больше, чем время окончания мониторинга
                    elif light_on >= end_control:
                        # Время начала освещения принимаем за время конца мониторинга
                        light_on = end_control
                        if show_hint: print(
                            "Время начала освещения комнаты больше, чем время окончания мониторинга: light_on = end_control = " + str(
                                end_control))

                    # Берем время выключения равное времени конца мониторинга
                    light_off = end_control

                    # Производим подсчет seconds
                    if show_hint: print("Производим подсчет seconds")
                    if show_hint: print("light_off = " + str(light_off))
                    if show_hint: print("light_on = " + str(light_on))
                    if show_hint: print(
                        "(light_off - light_on).total_seconds() = " + str((light_off - light_on).total_seconds()))
                    if show_hint: print("result = " + str(result))
                    if (light_off - light_on).total_seconds() > 0:
                        result += (light_off - light_on).total_seconds()
                    if show_hint: print("ИТОГО: " + str(result))
                # --------------------------
            # Если комната освещалась и перестала освещаться | или комната освещается и это последний временной элемент
            elif (not lights_room(def_lights, def_count_light) and last_status_lights) or \
                    (lights_room(def_lights, def_count_light) and (index == len(end_els) - 1)):
                if show_hint: print("=====(not lights_room(def_lights, def_count_light) and last_status_lights)=====")
                if show_hint: print("not lights_room(def_lights, def_count_light) = " + str(not lights_room(def_lights, def_count_light)))
                if show_hint: print("last_status_lights) = " + str(last_status_lights))
                if show_hint: print("-"*50)
                if show_hint: print("OR")
                if show_hint: print("-" * 50)
                if show_hint: print("===== (lights_room(def_lights, def_count_light) and (index == len(end_els) - 1)=====")
                if show_hint: print("lights_room(def_lights, def_count_light) = " + str(lights_room(def_lights, def_count_light)))
                if show_hint: print("index == len(end_els) - 1 = " + str(index == len(end_els) - 1))
                if show_hint: print("-" * 50)
                # Запоминаем время выключения
                light_off = lamp_time
                # Меняем последний статус свечения
                last_status_lights = False
                if show_hint: print("Комната освещалась и перестала освещаться или комната освещается и это последний временной элемент")
                if show_hint: print("light_off = lamp_time = " + str(lamp_time))
                if show_hint: print("last_status_lights = False")

                # Если время начала освещения комнаты раньше, чем время начала мониторинга
                if light_on <= start_control:
                    # Время начала освещения принимаем за время начала мониторинга
                    light_on = start_control
                    if show_hint: print("Время начала освещения комнаты раньше, чем время начала мониторинга: light_on = start_control = " + str(start_control))
                # Если время начала освещения комнаты больше, чем время окончания мониторинга
                elif light_on >= end_control:
                    # Время начала освещения принимаем за время конца мониторинга
                    light_on = end_control
                    if show_hint: print("Время начала освещения комнаты больше, чем время окончания мониторинга: light_on = end_control = " + str(end_control))

                # Если время окончания освещения комнаты больше, чем время конца мониторинга
                if light_off >= end_control:
                    # Время окончания освещения принимаем за время конца мониторинга
                    light_off = end_control
                    if show_hint: print("Время окончания освещения комнаты больше, чем время конца мониторинга: light_off = end_control = " + str(end_control))
                # Если комната освещается и больше не будет временных сигналов (он последний)
                elif lights_room(def_lights, def_count_light) and (index == len(end_els) - 1):
                    # Берем время выключения равное времени конца мониторинга
                    light_off = end_control
                    if show_hint: print("Комната освещается и больше не будет временных сигналов (он последний) light_off = end_control = " + str(end_control))

                # Производим подсчет seconds
                if show_hint: print("Производим подсчет seconds")
                if show_hint: print("(light_off - light_on).total_seconds() = " + str((light_off - light_on).total_seconds()))
                if show_hint: print("result = " + str(result))
                if (light_off - light_on).total_seconds() > 0:
                    result += (light_off - light_on).total_seconds()
                if show_hint: print("ИТОГО: " + str(result))
            if show_hint: print("=============================")

        if show_hint: print("=============================")
        if show_hint: print("Все временные отметки пройдены")
        if show_hint: print("result = " + str(result))
        if show_hint: print("=============================")
        return result

    # -/-/-/-/-/-/-/-/-/-/-/-/-/
    #       Основная логика
    # -/-/-/-/-/-/-/-/-/-/-/-/-/

    # Максимальное количество лампочек
    if show_hint: print("Максимальное количество лампочек")
    max_light = find_max_light(def_els=els)
    if show_hint: print("max_light = " + str(max_light))

    # Необходимое количество лампочек для освещения комнаты
    if show_hint: print("Необходимое количество лампочек для освещения комнаты")
    count_light = find_count_light(req)
    if show_hint: print("count_light = " + str(count_light))

    if show_hint: print("=" * 50)

    # Заполнение списка
    if show_hint: print("Заполнение списка лампочек")
    lights = fill_lights(max_light)
    for light in range(len(lights)):
        if show_hint: print(lights[light])

    if show_hint: print("=" * 50)

    if show_hint: print("СОЗДАНИЕ И СОРТИРОВКА НОВОГО СПИСКА")
    if show_hint: print("Исходный список:")
    if show_hint: print("-"*50)
    for k in range(len(els)):
        if show_hint: print(els[k])
    if show_hint: print("-" * 50)
    end_els = sort_els(all_signal())
    if show_hint: print("Полный список со всеми временными отметками + сортировка (end_els):")
    if show_hint: print("-" * 50)
    for z in range(len(end_els)):
        if show_hint: print(end_els[z])

    if show_hint: print("="*50)

    start_control = find_start_control(def_els=end_els, def_start_watching=start_watching)
    if show_hint: print("Время начала контроля (start_control) = " + str(start_control))

    if show_hint: print("="*50)

    end_control = find_end_control(def_els=end_els, def_end_watching=end_watching)
    if show_hint: print("Время окончания контроля (end_control) = " + str(end_control))

    if show_hint: print("="*50)

    # Заполнение списка
    if show_hint: print("Заполнение списка лампочек")
    lights = fill_lights(max_light)
    for light in range(len(lights)):
        if show_hint: print(lights[light])

    if show_hint: print("="*50)

    seconds = count_seconds(end_els, lights, count_light)

    if show_hint: print("seconds = " + str(seconds))
    return seconds


if __name__ == '__main__':
    print("Example:")

    print(sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 0, 50), 3),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3))

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ]) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 11, 0, 0), 2),
        (datetime(2015, 1, 12, 11, 1, 0), 2),
    ]) == 70

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ]) == 30

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ]) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 3),
        (datetime(2015, 1, 12, 10, 1, 20), 3),
    ]) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 50)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 30)) == 20

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 30

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 10)) == 30

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 50)) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 30)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 30

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], datetime(2015, 1, 12, 10, 0, 20)) == 50

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 30), datetime(2015, 1, 12, 10, 1, 0)) == 30

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 30)) == 30

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0)) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 0, 10)) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 30)) == 20

    assert sum_light(els=[
        (datetime(2015, 1, 11, 0, 0, 0), 3),
        datetime(2015, 1, 12, 0, 0, 0),
        (datetime(2015, 1, 13, 0, 0, 0), 3),
        (datetime(2015, 1, 13, 0, 0, 0), 2),
        datetime(2015, 1, 14, 0, 0, 0),
        (datetime(2015, 1, 15, 0, 0, 0), 2),
    ], start_watching=datetime(2015, 1, 10, 0, 0, 0), end_watching=datetime(2015, 1, 16, 0, 0, 0)) == 345600

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], operating=timedelta(seconds=100)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], operating=timedelta(seconds=5)) == 5

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=100)) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 30),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=100)) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 30),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], operating=timedelta(seconds=20)) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 0), 3),
        (datetime(2015, 1, 12, 10, 1, 20), 3),
    ], operating=timedelta(seconds=10)) == 30

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=10)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
        operating=timedelta(seconds=20)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
        operating=timedelta(seconds=10)) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 10), end_watching=datetime(2015, 1, 12, 10, 0, 30),
        operating=timedelta(seconds=5)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], req=1) == 60

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        (datetime(2015, 1, 12, 10, 0, 0), 2),
        datetime(2015, 1, 12, 10, 0, 10),
        (datetime(2015, 1, 12, 10, 1, 0), 2),
    ], req=2) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=1) == 40

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 50), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], req=3) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0), req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 0), datetime(2015, 1, 12, 10, 1, 0), req=2, operating=timedelta(seconds=15)) == 10

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=2) == 20

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=3) == 0

    assert sum_light([
        (datetime(2015, 1, 12, 10, 0, 0), 4),
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
        (datetime(2015, 1, 12, 10, 1, 20), 2),
        (datetime(2015, 1, 12, 10, 1, 40), 2),
    ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100), req=3) == 20

    print("The forth mission in series is completed? Click 'Check' to earn cool rewards!")