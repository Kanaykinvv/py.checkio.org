# Вам дан результат игры, и вы должны решить, кто победил или что это ничья. Ваша функция должна вернуть "X"
# если победил Х-игрок и "О" если победил О-игрок. В случае ничьи, результат должен быть "D".
#
# Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
#
# Вх. данные: Результат игры, как список (list) строк (str, unicode).
#
# Вых. данные: "X", "O" или "D", как строка (str).
#
# Примеры:
#
# checkio([
#     "X.O",
#     "XX.",
#     "XOO"]) == "X"
# checkio([
#     "OO.",
#     "XOX",
#     "XOX"]) == "O"
# checkio([
#     "OOX",
#     "XXO",
#     "OXX"]) == "D"
#
# Как это используется: Эта задача поможет вам лучше понять, как работать с матрицами и вложеными массивами.
# Ну и конечно, это будет полезно при разработке игр, так как надо уметь оценивать результаты.
#
# Предусловия:
# В играх может быть только один победитель или ничья.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)

from typing import List

def checkio(game_result: List[str]) -> str:
    """
    Функция определения победителя в игре "Крестики-Нолики"
    :param game_result: Входной список ходов (X - ход X; O - ход O; . - пусто)
    :return: Вывод результата (X - победитель X; O - победитель O; D - ничья)
    """
    show_hints = False

    if show_hints: print("=====START=====")

    dashboard = [
        [game_result[0][0], game_result[0][1], game_result[0][2]],
        [game_result[1][0], game_result[1][1], game_result[1][2]],
        [game_result[2][0], game_result[2][1], game_result[2][2]],
        ]

    if show_hints:
        for index in range(3):
            print(dashboard[index])

    x = 0
    o = 0

    if show_hints: print("---Find row-col---")
    for row in range(3):
        for col in range(3):
            if dashboard[row][col] == "X":
                x += 1
            elif dashboard[row][col] == "O":
                o += 1
            elif dashboard[row][col] == ".":
                break
        if x == 3:
            if show_hints: print("Winner X")
            return "X"
        if o == 3:
            if show_hints: print("Winner O")
            return "O"
        if show_hints: print("row = [" + str(row) + "] x = " + str(x))
        if show_hints: print("row = [" + str(row) + "] o = " + str(o))
        x = 0
        o = 0

    if show_hints: print("---Find col-row---")
    for col in range(3):
        for row in range(3):
            if dashboard[row][col] == "X":
                x += 1
            elif dashboard[row][col] == "O":
                o += 1
            elif dashboard[row][col] == ".":
                break
        if x == 3:
            if show_hints: print("Winner X")
            return "X"
        if o == 3:
            if show_hints: print("Winner O")
            return "O"
        if show_hints: print("col = [" + str(col) + "] x = " + str(x))
        if show_hints: print("col = [" + str(col) + "] o = " + str(o))
        x = 0
        o = 0

    if show_hints: print("---Find right-left---")
    for i in range(3):
        if dashboard[i][2-i] == "X":
            x += 1
        elif dashboard[i][2-i] == "O":
            o += 1
        elif dashboard[i][2-i] == ".":
            break
        if x == 3:
            if show_hints: print("Winner X")
            return "X"
        if o == 3:
            if show_hints: print("Winner O")
            return "O"
    if show_hints: print("x = " + str(x))
    if show_hints: print("o = " + str(o))

    x = 0
    o = 0

    if show_hints: print("---Find left-right---")
    for i in range(3):
        if dashboard[i][i] == "X":
            x += 1
        elif dashboard[i][i] == "O":
            o += 1
        elif dashboard[i][i] == ".":
            break
        if x == 3:
            if show_hints: print("Winner X")
            return "X"
        if o == 3:
            if show_hints: print("Winner O")
            return "O"
    if show_hints: print("x = " + str(x))
    if show_hints: print("o = " + str(o))

    if show_hints: print("Draw")
    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
