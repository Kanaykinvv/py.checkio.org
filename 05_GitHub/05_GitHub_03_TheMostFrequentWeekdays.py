# Вам дан год как целое число (например, 2001). Вы должны вернуть наиболее частые дни недели в этом году.
# Результатом должен быть список дней, отсортированный по порядку дней в неделе (например, [«Понедельник», «Вторник»]).
# Неделя начинается с понедельника.
#
# Входные данные: Год как целое число (int).
#
# Выходные данные: Список наиболее распространенных дней отсортированный по порядку дней в неделе
# (с понедельника по воскресенье).
#
# Пример:
#
# most_frequent_days(1084) == ['Tuesday', 'Wednesday']
# most_frequent_days(1167) == ['Sunday']
# 1
# 2
# Предварительные условия: Год является числом от 1 до 9999. Неделя начинается с понедельника.
from datetime import date

def most_frequent_days(year):
    result=[x[1] for x in sorted(set([(date(year,1,1).weekday(),date(year,1,1).strftime("%A")),\
    (date(year,12,31).weekday(),date(year,12,31).strftime("%A"))]))]
    return result


if __name__ == '__main__':
    print("Example:")
    print(most_frequent_days(1167))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert most_frequent_days(1084) == ['Tuesday', 'Wednesday']
    assert most_frequent_days(1167) == ['Sunday']
    assert most_frequent_days(1216) == ['Friday', 'Saturday']
    assert most_frequent_days(1492) == ['Friday', 'Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(212) == ['Wednesday', 'Thursday']
    assert most_frequent_days(1) == ['Monday']
    assert most_frequent_days(2135) == ['Saturday']
    assert most_frequent_days(3043) == ['Sunday']
    assert most_frequent_days(2001) == ['Monday']
    assert most_frequent_days(3150) == ['Sunday']
    assert most_frequent_days(3230) == ['Tuesday']
    assert most_frequent_days(328) == ['Monday', 'Sunday']
    assert most_frequent_days(2016) == ['Friday', 'Saturday']
    print("Coding complete? Click 'Check' to earn cool rewards!")
