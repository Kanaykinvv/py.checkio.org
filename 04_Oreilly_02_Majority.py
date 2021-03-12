# У нас есть список логических значений. Проверим, верны ли большинство элементов.
#
# пример
#
# Некоторые случаи, о которых стоит упомянуть:
# 1) пустой список должен возвращать false;
# 2) если истинность и ложь равны, функция должна возвращать ложь.
#
# Вход: список логических значений.
#
# Выход: логическое значение.
def is_majority(items: list) -> bool:
    # your code here
    if len(items) == 0:
        return False
    count_true = 0
    count_false = 0
    for item in items:
        if item == True:
            count_true += 1
        else:
            count_false += 1

    if count_true <= count_false:
        return False
    else:
        return True



if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
