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

    #replace this for solution
    return 'string representation of n'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
