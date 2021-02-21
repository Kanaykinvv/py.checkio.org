# У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
#
# Входные данные: Положительное целое число.
#
# Выходные данные: Целое число (0-9).
#
# Пример:
#
# max_digit(0) == 0
# max_digit(52) == 5
# max_digit(634) == 6
# max_digit(1) == 1
# max_digit(10000) == 1
def max_digit(number: int) -> int:
    # your code here
    max_num = 0
    str_number = str(number)
    for char in range(len(str_number)):
        if int(str_number[char]) > max_num:
            max_num = int(str_number[char])
    return max_num


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
