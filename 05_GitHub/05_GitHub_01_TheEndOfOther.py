# В этой задаче дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, такая что одно слово
# заканчивается другим (суффикс или совпадение). Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello",
# так что результат True.
#
# Замечания: Для этой задачи вы можете прочитать о типе данных set и строковых функциях.
#
# Вх. данные: Слова как набор (set) строк (str).
#
# Вых. данные: True или False, как булево выражение.
#
# Примеры:
#
# checkio({"hello", "lo", "he"}) == True
# checkio({"hello", "la", "hellow", "cow"}) == False
# checkio({"walk", "duckwalk"}) == True
# checkio({"one"}) == False
# checkio({"helicopter", "li", "he"}) == False

# Как это используется: В этой задаче вы познакомитесь с тем, как итерировать тип данных set и некоторыми
# полезными функциями.
#
# Предусловия: 2 ≤ len(words) < 30
# all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

def checkio(words_set):
    """
    Функция поиска совпадений окончаний слов по исходному набору
    :param words_set: Исходный набор
    :return: Результат поиска (True - в наборе есть совпадения, False - набор мал или нет совпадений)
    """
    if len(words_set) > 1:
        tmp_list = list(words_set)
        tmp_list.sort(key = lambda x: len(set(list(x))))
        print(tmp_list)
        for index in range(len(tmp_list) - 1):
            for i in range(len(tmp_list)):
                if (tmp_list[index] in tmp_list[i]) and (tmp_list[index] != tmp_list[i]):
                    if tmp_list[i][-1 * len(tmp_list[index]):] == tmp_list[index]:
                        return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
