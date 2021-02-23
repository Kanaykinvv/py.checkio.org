# Найдите ближайшее значение к переданному.
#
# Вам даны список значений в виде множества (Set) и значение, относительно которого, надо найти ближайшее.
#
# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17. И нам нужно найти ближайшее значение к цифре 9. Если отсортировать этот ряд по возрастанию, то слева от 9 будет 7, а справа 10. Но 10 - находится ближе, чем 7, значит правильный ответ 10.
#
# Несколько уточнений:
#
# Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# Ряд чисел всегда не пустой, т.е. размер >= 1;
# Переданное значение может быть в этом ряде, а значит оно и является ответом;
# В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# Ряд не отсортирован и состоит из уникальных чисел.
# Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
#
# Выходные данные: Int.
#
# Пример:
#
# nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
def nearest_value(values: set, one: int) -> int:
    # your code here
    if one in values:
        print(str(one) + " входит в набор " + str(values))
        print("Ответ = " + str(one))
        return one
    else:
        print("one = " + str(one))
        print(str(one) + " не входит в набор " + str(values))
        list_values = list(values)
        list_values.sort()
        print("создали новый список из набора и отсортировали его: " + str(list_values))
        result_min = min(list_values)
        print("result_min = " + str(result_min))
        result_max = max(list_values)
        print("result_max = " + str(result_max))

        if (one < result_min) and (one < result_max):
            print("one меньше любых чисел в наборе")
            print("Ответ = " + str(result_min))
            return result_min
        elif (result_min < one) and (result_max < one):
            print("one больше любых чисел в наборе")
            print("Ответ = " + str(result_max))
            return result_max

        print("one входит в диапазон набора")
        print("------------------------------")
        print("Начало цикла поиска")
        for i in range(len(list_values) - 1):
            print("----------Цикл----------")
            print("i = " + str(i))
            print("list_values[" + str(i) + "] = " + str(list_values[i]))
            print("list_values[" + str(i+1) + "] = " + str(list_values[i+1]))
            print("one = " + str(one))

            if (list_values[i] < one) and (one < list_values[i+1]):
                print("Сработало правило 1: (list_values[i] < one) and (one < list_values[i+1])")
                print("one входит между 2-х чисел")
                result_min = list_values[i]
                result_max = list_values[i+1]
                print("result_min = " + str(result_min))
                print("result_max = " + str(result_max))
                print("выход из цикла перебора")
                break
            else:
                print("В текущем цикле ни одно праввило не сработало")

        print("проверка разницы: (one - result_min) < (result_max - one)")
        print("one = " + str(one))
        print("result_min = " + str(result_min))
        print("result_max = " + str(result_max))
        if (one - result_min) < (result_max - one):
            print("Выбор: result_min")
            print("Ответ = " + str(result_min))
            print(str(result_min))
            return result_min
        elif (one - result_min) == (result_max - one):
            print("растояние до result_min и result_max одинаково - Выбор: result_min")
            print("Ответ = " + str(result_min))
            print(str(result_min))
            return result_min
        else:
            print("Выбор: result_max")
            print("Ответ = " + str(result_max))
            print(str(result_max))
            return result_max


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
