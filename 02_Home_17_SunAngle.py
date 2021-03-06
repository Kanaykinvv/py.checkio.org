# Ваша задача - определить угол солнца над горизонтом, зная время суток. Исходные данные: солнце встает на востоке
# в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце
# садится за горизонт и угол равен 180 градусов. В случае, если указано ночное время (раньше 6:00 или позже 18:00),
# функция должна вернуть фразу "I don't see the sun!".
#
# example
#
# Входные данные: Время.
#
# Выходные данные: Угол солнца над горизонтом, округленный до 2 знаков после запятой.
#
# Пример:
#
# sun_angle("07:00") == 15
# sun_angle("12:15"] == 93.75
# sun_angle("01:23") == "I don't see the sun!"

# Как это используется: Жизненно необходимый навык для любого путешественника, особенно в случае утери компаса и
# разрядившегося мобильного телефона с GPS. Правда, в такой ситуации приходится решать обратную задачу - определять
# время по углу солнца и производить несколько дополнительных расчетов.
#
# Предусловия:
# 00:00 <= время <= 23:59
def sun_angle(time):
    #replace this for solution
    if ("06:00" <= time) and (time <= "18:00"):
        hour = int(time[0:2])
        min = int(time[3:])
        all_min = (hour - 6 ) * 60 + min
        angle = (180 * all_min) / 720
        return angle
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("17:39"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
