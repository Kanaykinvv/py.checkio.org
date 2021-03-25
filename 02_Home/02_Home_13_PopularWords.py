# Ваша задача в этой миссии определить популярность определенных слов в тексте.
#
# На вход вашей функции передается 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
#
# При решении этой задачи обратите внимание на следующие моменты
#
# Слова необходимо искать во всеx регистрах. Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
# Искомые слова всегда указаны в нижнем регистре
# Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
# Входные параметры: Текст и массив искомых слов.
#
# Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.
#
# Пример:
#
# popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#     'i': 4,
#     'was': 3,
#     'three': 0,
#     'near': 0
# }
#
# Предусловия:
# Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.
import re


def popular_words(text: str, words: list) -> dict:
    list_text = re.split('\s', text.lower())

    for word in range(0, len(words)):
        words[word] = str(words[word]).lower()

    result = dict.fromkeys(words, 0)

    for i in range(0, len(list_text)):
        if list_text[i] in result.keys():
            key = list_text[i]
            volue = result.get(list_text[i]) + 1
            result.update({key: volue})
    return result

if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'whree', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")