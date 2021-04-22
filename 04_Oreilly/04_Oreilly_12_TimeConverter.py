# Вы современый человек, предпочитающий использовать 24-часовой формат времени.
# Но в некоторых регионах используют 12-часовой формат. Ваша задача - переконвертировать
# время из 12-часового формата в 24-часовой, используя следующие правила:
# - выходной формат должен быть 'чч:мм'
# - если часы меньше 10 - допишите '0' перед ними. Например: '09:05'
# Вы можете узнать больше подробностей о 12-часовом формате.
#
# Входные данные: Время в 12-часовом формате (как строка).
#
# Выходные данные: Время в 24-часовом формате (как строка).
#
# Примеры:
#
# time_converter('12:30 p.m.') == '12:30'
# time_converter('9:00 a.m.') == '09:00'
# time_converter('11:15 p.m.') == '23:15'
# Как это используется: Для работы с разными форматами времени.
#
# Предусловия:
# '00:00' <= время <= '23:59'

def time_converter(time):
    #replace this for solution
    time_list = time.split()

    hour = time_list[0][:time_list[0].find(':')]
    minutes = time_list[0][time_list[0].find(':') + 1:]

    if int(hour) < 10:
        hour = "0" + hour

    print("Часы = " + hour)
    print("Минуты = " + minutes)


    # return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))
    #
    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert time_converter('12:30 p.m.') == '12:30'
    # assert time_converter('9:00 a.m.') == '09:00'
    # assert time_converter('11:15 p.m.') == '23:15'
    # print("Coding complete? Click 'Check' to earn cool rewards!")