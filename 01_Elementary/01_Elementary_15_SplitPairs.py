# Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
#
# Входные данные: Строка.
#
# Выходные данные: Массив строк.
#
# Пример:
#
# split_pairs('abcd') == ['ab', 'cd']
# split_pairs('abc') == ['ab', 'c_']
# 1
# 2
# Предварительное условие: 0<=len(str)<=100
def split_pairs(a):
    # your code here
    str_list = list()
    if 0 <= len(a) <= 100:
        while len(a) > 0:
            if len(a) == 1:
                str_list.append(a[0] + '_')
                a = ''
            if len(a) >= 2:
                str_list.append(a[0:2])
                a = a[2::]
        return str_list
    else:
        return []


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
