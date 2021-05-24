# Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел. Для него сейчас большая проблема
# произносить составные числа. Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу. Стефан
# должен говорить на английском, так что вам нужно знать правила составления чисел в английском языке. Все слова в
# строковом представлении числа должны быть разделены одним пробелом. Будьте осторожны с пробелами -- очень сложно
# увидеть двойной пробел, но это критично для компьютера.
#
# Вх. данные: Число, как целочисленное (int).
#
# Вых. данные: Текстовое написание числа, как строка (str).
#
# Примеры:
#
# checkio(4)=='four'
# checkio(143)=='one hundred forty three'
# checkio(12)=='twelve'
# checkio(101)=='one hundred one'
# checkio(212)=='two hundred twelve'
# checkio(40)=='forty'

# Как это используется: Эта концепция будет полезна для программного обеспечения по синтезу речи или автоматических
# систем отчетности. Также это может пригодиться при написании простого бота для чата, который будет уметь составлять
# числа.
#
# Предусловия: 0 < number < 1000
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    """
    Функция перевода цифровой записи числа в буквенную.
    :param number: Запись числа цифрами (1-999)
    :return: Строчная запись числа
    """
    # Для определения количества разрядов в числе, переводим ее в строку
    number_str = str(number)

    # Количество соток, десяток и единиц
    xxx, xx, x = 0, 0, 0

    # Если число от 100
    if len(number_str) == 3:
        # Высчитываем количество соток, десяток и единиц
        xxx = number // 100
        xx = (number - (xxx * 100)) // 10
        x = number - (xxx * 100) - (xx * 10)
    # Если число меньше 100
    elif len(number_str) == 2:
        # Высчитываем количество десяток и единиц
        xx = number // 10
        x = number - (xx * 10)
    # Если число меньше 10
    elif len(number_str) == 1:
        # Количество единиц равно числу
        x = number

    # Для результата
    result = ""

    # Если есть сотки, включаем их запись в результ
    if xxx > 0:
        result = FIRST_TEN[xxx - 1] + " " + HUNDRED

    # Если десяток один, включаем в результат от 10 до 19
    if xx == 1:
        # Если были сотки
        if len(result) > 0:
            result += " " + SECOND_TEN[x]
        # Если соток не было
        else:
            result = SECOND_TEN[x]
    # Если десятков больше одного, записываем в результат от 20 до 90, и при наличии количество единиц
    elif xx > 1:
        # Если были сотки
        if len(result) > 0:
            # Десятки
            result += " " + OTHER_TENS[xx - 2]
            # Единицы
            if x > 0:
                result += " " + FIRST_TEN[x - 1]
        # Если соток не было
        else:
            # Десятки
            result = OTHER_TENS[xx - 2]
            # Единицы
            if x > 0:
                result += " " + FIRST_TEN[x - 1]
    # Если десятков нет, проверяем количество единиц
    elif xx == 0:
        # Если были сотки
        if len(result) > 0:
            # Единицы
            if x > 0:
                result += " " + FIRST_TEN[x - 1]
        # Если соток не было
        else:
            # Единицы
            if x > 0:
                result = FIRST_TEN[x - 1]

    # Выводим результат
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    # print('Done! Go and Check it!')
