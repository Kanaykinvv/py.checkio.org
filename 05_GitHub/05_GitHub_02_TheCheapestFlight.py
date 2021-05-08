# На входе вы получаете расписание самолетов в виде массива, каждый элемент которого это цена прямого воздушного
# соединения 2х городов (массив из 3х элементов - 2 названия города, в виде строки, и цена перелета).
#
# Самолеты летают в обе стороны и цена в обе стороны одинаковая. Есть вероятность, что соединения между городами
# может и не быть.
#
# Найдите цену самого дешевого перелета для городов, которые переданы 2ым и 3им аргументами.
#
# Input: 3 аргумента. Расписание перелетов в виде массива массивов. Город вылета и город назначения.
#
# Output: Int. Лучшая цена.
#
# Example:
#
# cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['B', 'C', 50]],
#  'A',
#  'C') == 70
# cheapest_flight([['A', 'C', 100],
#   ['A', 'B', 20],
#   ['B', 'C', 50]],
#  'C',
#  'A') == 70

# Как это используется: Может быть использовано в повседневной жизни для нахождения оптимальной комбинации.
#
# Precondition: Цена всегда int. В расписании рейсов есть хотя бы один элемент. Оба искомых города есть в расписании.
from typing import List


def cheapest_flight(costs: List, a: str, b: str) -> int:
    # "Алгоритм Дейкстры"
    # https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%94%D0%B5%D0%B9%D0%BA%D1%81%D1%82%D1%80%D1%8B
    show_hints = True

    # Прямой (False) или обратный (True) поиск пути
    revers = True if a > b else False
    if show_hints: print("revers = " + str(revers))

    # Начальная вершина имеет вес равный 0
    weights = {a: 0}
    # if revers:
    #     weights = {b: 0}
    # else:
    #     weights = {a: 0}

    if show_hints: print("weights = " + str(weights))

    # Остальные вершины максимальный вес
    for cost in costs:
        if cost[0] not in weights.keys():
            weights[cost[0]] = int(2**32)
        if cost[1] not in weights.keys():
            weights[cost[1]] = int(2**32)

    if show_hints: print(weights)

    # Множество посещенных вершин (на старте пустое)
    visitedPeaks = set()

    # Нахождение вершины с минимальным весом
    def search_min_unvisited_peaks() -> str:
        """
        Нахождение вершины с минимальным весом
        :return: Имя вершины с минимальным весом
        """
        current_element = ""
        current_weight = 2**32
        if show_hints: print("-"*50)
        for key in weights.keys():
            if show_hints: print("key = " + str(key))
            if (key not in visitedPeaks) and (weights[key] <= current_weight):
                if show_hints: print("Вершина не посещена и ее вес меньше:")
                current_element = key
                current_weight = weights[key]
                if show_hints: print("current_element = " + str(current_element))
                if show_hints: print("current_weight = " + str(current_weight))
        if show_hints: print("current_element найден: " + str(current_element))
        if show_hints: print("-" * 50)
        return current_element

    while len(visitedPeaks) != len(weights.keys()):
        if show_hints: print("-" * 50)
        element = search_min_unvisited_peaks()
        if show_hints: print("element = " + str(element))
        # Проходим все входные списки
        for cost in costs:
            if show_hints: print("cost = " + str(cost))
            if not revers:
                if show_hints: print("not revers")
                # Находим стартовую текущую точку
                if cost[0] == element:
                    if show_hints: print("cost[0] == element = " + str(element))
                    # Находим наименьший вес до второй точки
                    if cost[2] + weights[element] <= weights[cost[1]]:
                        if show_hints: print("cost[2] + weights[element] = " + str(cost[2]) + " + " + str(weights[element]) + " <= weights[cost[1] = " + str(weights[cost[1]]) + "]")
                        weights[cost[1]] = cost[2] + weights[element]
                        if show_hints: print("weights[cost[1]] = " + str(weights[cost[1]]))
            else:
                if show_hints: print("revers")
                # Находим стартовую текущую точку
                if cost[1] == element:
                    if show_hints: print("cost[1] == element = " + str(element))
                    # Находим наименьший вес до второй точки
                    if cost[2] + weights[element] <= weights[cost[0]]:
                        if show_hints: print("cost[2] + weights[element] = " + str(cost[2]) + " + " + str(weights[element]) + " <= weights[cost[0] = " + str(weights[cost[0]]))
                        weights[cost[0]] = cost[2] + weights[element]
                        if show_hints: print("weights[cost[0]] = " + str(weights[cost[0]]))
            if show_hints: print("-" * 25)

        # Отмечаем вершину как пройденную
        if show_hints: print("visitedPeaks.add(" + str(element) + ")")
        visitedPeaks.add(element)
        if show_hints: print("visitedPeaks = " + str(visitedPeaks))


    # print(weights[b]) if not revers else print(weights[a])
    #
    # return weights[b] if not revers else weights[a]
    return weights[b]

# Не правильный счет при реверсе поиска


if __name__ == '__main__':
    # print("Example:")
 #    print(cheapest_flight([['A', 'C', 100],
 #  ['A', 'B', 20],
 #  ['B', 'C', 50]],
 # 'A',
 # 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
 #    assert cheapest_flight([['A', 'C', 100],
 #  ['A', 'B', 20],
 #  ['B', 'C', 50]],
 # 'A',
 # 'C') == 70
 #    assert cheapest_flight([['A', 'C', 100],
 #  ['A', 'B', 20],
 #  ['B', 'C', 50]],
 # 'C',
 # 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
 #    assert cheapest_flight([['A', 'C', 100],
 #  ['A', 'B', 20],
 #  ['D', 'F', 900]],
 # 'A',
 # 'F') == 0
 #    assert cheapest_flight([['A', 'B', 10],
 #  ['A', 'C', 15],
 #  ['B', 'D', 15],
 #  ['C', 'D', 10]],
 # 'A',
 # 'D') == 25
 #    print("Coding complete? Click 'Check' to earn cool rewards!")
