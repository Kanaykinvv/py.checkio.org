# Из множества(set) целых чисел(int) вам нужно создать список(list) замкнутых интервалов в виде кортежей(tuple) таких,
# чтобы интервалы охватывали все значения, найденные в множестве.
#
# Замкнутый интервал включает в себя конечные точки! Интервал 1..5 , например, включает каждое значение x , которое
# удовлетворяет условию: 1 <= x <= 5.
#
# Значения могут быть в одном интервале только если разность между значением и следующим меньшим значением в наборе
# равно единице, иначе начинается новый интервал.
# Отдельное значение, которое не вписывается в существующие правила формирования интервалов, становится начальной и
# конечной точкой нового интервала.
#
# Входящие данные: множество(set) целых чисел(int).
#
# Исходящие: список кортежей двух целых чисел(A list of tuples of two ints), обозначающими концы промежутка.
# Массив должен быть отсортирован по начальной точке каждого интервала.
#
# Примеры:
#
# create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
# create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

def create_intervals(data):
    """
    Функция создания списка кортежей по входным отметкам.
    :param data: Входной перечень отметок
    :return: Список кортежей
    """
    result = []         # Результат
    show_hits = False   # Подсказки

    # Из-за ошибки проверки на сайте, пришлось внедрить такой костыль (на проверку поступал список списков)
    if type(data) == list:
        data_list = sorted(data)
        if show_hits: print("list")
    else:
        if show_hits: print("not list")
        data_list = sorted(list(data))

    if show_hits: print("Исходный список: " + str(data_list))

    if len(data_list) > 0:

        start = data_list[0]
        if show_hits: print("Исходный start = " + str(start))

        for i in range(len(data_list)):
            if show_hits: print("-"*50)
            if show_hits: print("i = " + str(i) + " | " + str(len(data_list)))

            if i == len(data_list) - 1:
                if show_hits: print("Это последний элемент data_list[" + str(i) + "] = " + str(data_list[i]))
                result.append((start, data_list[i]))
                if show_hits: print("Добавляем (" + str(start) + ", " + str(data_list[i]) + ")")

            elif (data_list[i] + 1) != data_list[i+1]:
                if show_hits: print("Текущий элемент data_list[" + str(i) + "] = " + str(data_list[i]) + " (+1) не равен следующему элементу data_list[" + str(i+1) + "] = " + str(data_list[i+1]))
                result.append((start, data_list[i]))
                if show_hits: print("Добавляем (" + str(start) + ", " + str(data_list[i]) + ")")
                start = data_list[i+1]
                if show_hits: print("Новое значение start = " + str(start))
            else:
                if show_hits: print("Текущий элемент data_list[" + str(i) + "] = " + str(data_list[i]) + " (+1) равен следующему элементу data_list[" + str(i+1) + "] = " + str(data_list[i+1]))

    if show_hits: print(result)

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals({8, 10, 12}) == [(8, 8), (10, 10), (12, 12)], "Therd"
    # assert create_intervals([8, 7]) == [[7, 8]],  "Error in Site"
    print('Almost done! The only thing left to do is to Check it!')
