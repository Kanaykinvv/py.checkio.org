# Отсортируйте данный итератор таким образом, чтобы его элементы оказались в порядке убывания частоты их появления,
# то есть по количеству раз, которое они появляются в элементах. Если два элемента имеют одинаковую частоту, они должны
# оказаться в том же порядке, в котором стояли изначально в итераторе.
#
# Входные данные: Итератор
#
# Выходные данные: Итератор
#
# Пример:
#
# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
# 1
# 2
# Предварительное условие: Элементы могут быть целыми числами или строками.
#
# Миссия была взята из Python CCPS 109 Осень 2018. Она преподается Илккой Коккариненым в Школа непрерывного образования
# Раймонда Чанга.
def frequency_sort(items):
    # your code here
    dict_items = dict()

    for item in items:
        if item not in dict_items.keys():
            dict_items[item] = 1
        else:
            dict_items[item] += 1

    result_list = list(dict_items.items())
    result_list.sort(key=lambda i: i[1], reverse=True)

    result = list()
    if len(result_list) > 0:
        for i in range(0, len(result_list)):
            for x in range(0, result_list[i][1]):
                result.append(result_list[i][0])

    return result



if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    # print(frequency_sort([4, 2, 2, 6, 4, 4, 4, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
