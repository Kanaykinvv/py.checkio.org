# Ваше задание - пересортировать список, расположив числа в порядке уменьшения их количества в списке.
# Если несколько чисел встречаются одинаково часто - их необходимо расположить в порядке от меньшего к большему,
# вне зависимости от того, в каком порядке они встречаются в исходном списке.
# Например: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]
#
# example
#
# Входные данные: Хаотичный набор чисел.
#
# Выходные данные: Список, отсортированный в зависимости от количества каждого числа в списке.
#
# Пример:
#
# frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]

# Как это используется: Для анализа данных с помощью математической статистики и мат.анализа,
# а также для нахождения тенденций и предсказания будущих изменений (систем, явлений и т.д.)
#
# Предусловия:
# array length <= 100
# max number <= 100
def frequency_sorting(numbers):
    #replace this for solution
    all_numbers = set()
    count = dict()

    for number in numbers:
        if number in all_numbers:
            count[number] += 1
        else:
            all_numbers.add(number)
            count[number] = 1

    # Временный список
    tmp_list = list()

    # Окончательный список
    result = list()

    # Пока есть элементы в count будем выполнять цикл
    while True:
        # Находим максимальное значение
        max_count = max(count.values())

        # Перебираем весь словарь
        for key, value in count.items():
            # Проверяем, если значение равно найденному максимальному значению
            if value == max_count:
                # то добавляем ключ по этому значению во временный список
                tmp_list.append(key)


        # Сортируем временный список (т.к. значений с одним количеством появлений может быть несколько
        # и тогда необходимо выводить их в порядке возрастания)
        tmp_list = sorted(tmp_list)

        # определяем количество итераций по количеству элементов во временном списке
        for element in range(0, len(tmp_list)):
            a = tmp_list[element]
            # определяем количество вставок
            for i in range(0, max_count):
                # добавляем в окончательный список элемент по количеству повторов
                result.append(tmp_list[element])
            # Удаляем из словаря элемент по ключу element
            del count[a]

        tmp_list.clear()

        if len(count.keys()) == 0:
            break

    # Возвращаем результат
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
