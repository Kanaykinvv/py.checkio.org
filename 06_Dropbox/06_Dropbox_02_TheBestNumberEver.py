# Это была версия Шелдона и его лучший номер. Но у вас есть навыки программирования, чтобы доказать, что есть
# лучшее число, или доказать Шелдон Шелдон прав. Вы можете вернуть любое число, но использовать код для доказательства
# вашего номера лучше!
#
# Эта миссия довольно проста для решения. Вам предоставляется функция под названием "checkio", которая будет
# возвращать любое число (целое или с плавающей точкой).
#
# Давайте писать сочинение в коде питона, который будет объяснять, почему это ваше число лучше. Публикация решения
# будет по умолчанию, и даст вам только 0 очков и цель, чтобы заработать очки через голоса за ваше эссе в коде.
#
# Входные данные: Ничего.
#
# Выходные данные: Число как целое или вещественное или комплексное.
#
# Примеры:
# isinstance(checkio(), (int, float, complex))
# Как это используется: Эта задача - это ваше сочинение в коде и программирование, как литература.
import random

def checkio():
    """
    Операция Капрекара.
    В 1949 году математик Д. Р. Капрекар из Деолали, Индия, разработал процесс, известный теперь как операция Капрекара.
    Сначала выберем четырехзначное число, состоящее хотя бы из двух различных цифр. Затем переставим его цифры, чтобы
    получить самое большое и самое маленькое из возможных чисел, образованных цифрами этого числа. Наконец, вычтем самое
    маленькое число из самого большого, получим новое число, для которого снова повторим операцию.
    Когда мы получим число 6174, операция повторяется, каждый раз давая 6174.
    :return: 6174
    """
    result = random.randint(1001, 9988)
    iteration = 0
    show_hint = False

    def minus_maxi_mini(x: int) -> int:
        list_int = list(char for char in str(x))
        maxi = "".join([str(item) for item in sorted(list_int, reverse=True)])
        mini = "".join([str(item) for item in sorted(list_int, reverse=False)])
        if show_hint: print("enter integer = " + str(x))
        if show_hint: print("maxi = " + str(maxi))
        if show_hint: print("mini = " + str(mini))
        if show_hint: print("outer integer = " + str(int(maxi) - int(mini)))
        return int(maxi) - int(mini)

    while result != 6174:
        result = minus_maxi_mini(result)
        iteration += 1
        if show_hint: print("iteration = " + str(iteration))
        if show_hint: print("-"*50)
        if iteration > 10:
            break

    if show_hint: print("final iteration = " + str(iteration))

    return 6174

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
