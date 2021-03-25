# Вам дана строка состоящая только из цифр. Вам нужно посчитать сколько нулей ("0") находится в начале строки.
#
# Входные данные: Строка, состоящая только из цифр.
#
# Выходные данные: Целое число.
#
# Пример:
#
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4
# Строка может иметь цифры: 0-9
def beginning_zeros(number: str) -> int:
    # your code here
    count_zero = 0
    start_search = True
    if len(number) > 0:
        for char in range(len(number)):
            if number[char] == '0' and start_search:
                count_zero += 1
            else:
                start_search = False
    return count_zero


if __name__ == '__main__':
    print("Example:")
    print(beginning_zeros('100'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert beginning_zeros('100') == 0
    assert beginning_zeros('001') == 2
    assert beginning_zeros('100100') == 0
    assert beginning_zeros('001001') == 2
    assert beginning_zeros('012345679') == 1
    assert beginning_zeros('0000') == 4
    print("Coding complete? Click 'Check' to earn cool rewards!")
