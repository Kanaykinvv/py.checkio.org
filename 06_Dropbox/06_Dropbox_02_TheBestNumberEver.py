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
    x = random.randint(1000, 9999)
    list_int = list(char for char in str(x))
    maxi = "".join([str(item) for item in sorted(list_int, reverse=True)])
    mini = "".join([str(item) for item in sorted(list_int, reverse=False)])

    print(maxi)
    print(mini)

    return 73  # if you are Sheldon

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio(), (int, float, complex))
