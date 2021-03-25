# Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.
#
# Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims". Если бы нам надо было
# найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать, что "s" – это самый
# первый символ в слове "sims", а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую "s", а она
# 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.
#
# Input: Две строки (String).
#
# Output: Int or None
#
# Примеры:
#
# second_index("sims", "s") == 3
# second_index("find the river", "e") == 12
# second_index("hi", " ") is None
import re
def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    result = [(m.start(0), m.end(0)) for m in re.finditer(symbol, text)]
    if len(result) >= 2:
        return result[1][0]
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
