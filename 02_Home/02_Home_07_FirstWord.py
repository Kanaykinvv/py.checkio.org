# Дана строка и нужно найти ее первое слово.
#
# При решении задачи обратите внимание на следующие моменты:
#
# В строке могут встречатся точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
# Входные параметры: Строка.
#
# Выходные параметры: Строка.
#
# Пример:
#
# first_word("Hello world") == "Hello"
# first_word("greetings, friends") == "greetings"
# 1
# 2
# How it is used: first word is a command in command line
#
# Precondition: text can contain a-z A-Z , . '
import re


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    list_text = re.split('\s|\.|,', text)
    result = ""
    for word in list_text:
        if word.isascii() and word != "":
            result = word
            break
    return result

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
