# Никола построил простого робота для покраски стены. Стена размечена через каждый метр и каждый участок пронумерован.
# Роботу для работы дан список действий. Каждая операция описывает какой участок стены необходимо покрасить, как два
# числа - откуда и докуда включительно. Для примера, операция [1, 5] означает, что будет покрашены секции от 1 до 5
# включительно. Операции исполняются в том порядке, как они даны в списке. Если некоторые операции окрашивают один
# и тот же участок стены, то они считаются, как окрашенные один раз.
#
# Стефан приготовил список действий для робота, но нам стоит проверить его прежде чем запускать робота.
# Вам дано суммарная длина участка (участков) стены в метрах, который должен быть окрашен (окрашенные участки
# могут разделятся неокрашеным) и список операций приготовленных Стефаном. Вам необходимо определить сколько
# операций из этого списка достаточно, чтобы окрасить необходимую длину. Если это невозможно с данным списком,
# то функция должна возвращать -1.
#
# Входные данные: Два аргумента.
#
# Необходимая длина участка (участков) стены для окраски, как целое число (int).
# Список операций, как список (list) списков целых чисел (int).
# Выходные данные: Минимальное достаточное число операций, как целое число (int) или -1, если это невозможно.
#
# Примеры:
# checkio(5, [[1,5], [11,15], [2,14], [21,25]]) == 1 # The first operation will paint 5 meter long.
# checkio(6, [[1,5], [11,15], [2,14], [21,25]]) == 2 # The second operation will paint 5 meter long. The sum is 10.
# checkio(11, [[1,5], [11,15], [2,14], [21,25]]) == 3 # After the third operation, the range 1-15 will be painted.
# checkio(16, [[1,5], [11,15], [2,14], [21,25]]) == 4 # Note the overlapped range must be counted only once.
# checkio(21, [[1,5], [11,15], [2,14], [21,25]]) == -1 # There are no ways to paint for 21 meters from this list.
#
# checkio(1000000011,[[1,1000000000],[11,1000000010]]) == -1 # One of the huge test cases.

# Зачем это надо: Эта задача демонстрирует вам, как можно использовать программирование для моделирования различных
# процессов. Теперь можем построить модель Тома Сойера.
#
# Предусловия:
# 0 < len(operations) ≤ 30
# all(0 < x < 2 * 10 ** 18 and 0 < y < 2 * 10 ** 18 for x, y in operations)
# 0 < required < 2 * 10 ** 18


def checkio(required, operations):

    current_operation = 0
    length = 0
    show_hint = False

    for oper in operations:
        if max(oper) > length:
            length = max(oper)

    if required > length:
        if show_hint: print("required > length = -1")
        return -1

    mass = [0] * length

    def metr_color(m: list) -> int:
        result = 0
        for i in range(len(m)):
            if m[i] == 1:
                result += 1
        return result

    if show_hint: print(mass)

    for operation in operations:
        for x in range(operation[0] - 1, operation[1]):
            mass[x] = 1
        if show_hint: print(mass)
        if show_hint: print("max_color(mass) = " + str(metr_color(mass)))
        current_operation += 1
        if metr_color(mass) >= required:
            if show_hint: print("metr_color(mass) >= required")
            return current_operation
    if show_hint: print("Final = -1")
    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    # assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    # assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    # assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    # assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    # assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
    assert checkio(30, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]) == 6, "test in site"

    # checkio(10000000000000, [[183456789012345, 193456789078479], [163456789034827, 173456789028737], [103456789038198, 113456789073490], [123456789073249, 203456789073621]])