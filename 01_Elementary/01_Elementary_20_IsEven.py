# Проверить является ли число четным или нет. Ваша функция должна возвращать True если число четное, и False если число не четное.
#
# Входные данные: Целое число.
#
# Выходные данные: Логический тип.
#
# Пример:
#
# is_even(2) == True
# is_even(5) == False
# is_even(0) == True
# 1
# 2
# 3
# Где это используется: (математика используется везде)
#
# Условия: целые числа даны в диапазоне от -1000 и до 1000
def is_even(num: int) -> bool:
    # your code here
    return True if (num % 2) == 0 else False


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
