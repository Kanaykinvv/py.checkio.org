# ана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера,
# в строке "start 5 one two three 7 end" есть три слова подряд.
#
# Входные данные: Строка со словами (str).
#
# Выходные данные: Ответ как логическое выражение (bool), True или False.
#
# Примеры:
#
# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False
#
# Зачем это нужно: Эта задача подскажет вам как работать со строками и покажет некоторые полезные функции.
#
# Предусловия: Исходная строка содержит только слова и/или числа. Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100
def checkio(words: str) -> bool:
    list_words = words.split(" ")
    count_words = 0
    for word in list_words:
        if count_words < 3:
            if word.isdigit():
                count_words = 0
            else:
                count_words += 1
    return True if count_words == 3 else False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
