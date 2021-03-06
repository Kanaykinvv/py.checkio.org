# Вам предоставляется набор координат, в которых расставлены белые пешки. Вы должны подсчитать количество защищенных
# пешек.
#
# Входные данные: Координаты расставленных пешек в виде набора строк.
#
# Выходные данные: Количество защищенных пешек в виде целого числа.
#
# Пример:
#
# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
# safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

# Как это используется: Для игрового искусственного интеллекта оценка текущего состояния в игре является одной из
# важных задач. Эта методика покажет вам как можно реализовать это для расстановок шахматных фигур.
#
# Предусловия:
# 0 < pawns ≤ 8
def safe_pawns(pawns: set) -> int:
    list_pawns = list(pawns)
    count = set()

    for pawn in list_pawns:
        letter = pawn[0]
        number = int(pawn[1])
        if letter == "a":
            if "b"+str(number-1) in pawns:
                count.add(pawn)
        elif letter == "b":
            if ("a" + str(number - 1) in pawns) or ("c" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "c":
            if ("b" + str(number - 1) in pawns) or ("d" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "d":
            if ("c" + str(number - 1) in pawns) or ("e" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "e":
            if ("d" + str(number - 1) in pawns) or ("f" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "f":
            if ("e" + str(number - 1) in pawns) or ("g" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "g":
            if ("f" + str(number - 1) in pawns) or ("h" + str(number - 1) in pawns):
                count.add(pawn)
        elif letter == "h":
            if "g" + str(number - 1) in pawns:
                count.add(pawn)

    return len(count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")