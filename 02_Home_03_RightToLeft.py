# "На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
# Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
#
# "Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше
# всего охарактеризовать, как "симметричные"."
# Scientific American. www.scientificamerican.com
#
# Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания
# инструкции по обходу корабля. Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
#
# Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
# даже если это часть другого слова. Все строки даны в нижнем регистре.
#
# Входные данные: Последовательность строк.
#
# Выходные данные: Текст, как строка.
#
# Пример:
#
# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
# left_join(("brightness wright",)) == "bleftness wleft"
# left_join(("enough", "jokes")) == "enough,jokes"
#
# Как это используется: Это просто пример операций, использующих строки и последовательности.
#
# Предусловие:
# 0 < len(phrases) < 42
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    result = ""
    for i in range(0, len(phrases)):
        if phrases[i].find("right") > -1:
            result += phrases[i].replace("right", "left")
        else:
            result += str(phrases[i])

        if i != (len(phrases) - 1):
            result += ","
    return result


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
