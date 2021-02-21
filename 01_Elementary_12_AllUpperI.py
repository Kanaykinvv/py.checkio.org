# Проверить все ли символы в строке являются заглавными. Если строка пустая или в ней нет букв - функция должна
# вернуть True.
#
# Входные данные: Строка.
#
# Выходные данные: Логический тип.
#
# Пример:
#
# is_all_upper('ALL UPPER') == True
# is_all_upper('all lower') == False
# is_all_upper('mixed UPPER and lower') == False
# is_all_upper('') == True
# 1
# 2
# 3
# 4
# Условия: a-z, A-Z, 1-9 и пробелы

def is_all_upper(text: str) -> bool:
    # your code here
    result = True
    if len(text) == 0 or text.strip(" "):
        result = True
    text_list = text.split(" ")
    for word in text_list:
        count_lower = 0
        for letter in word:
            if letter.islower():
                count_lower += 1
        if count_lower > 0:
            result = False
            break
    return result


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('Hi') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
