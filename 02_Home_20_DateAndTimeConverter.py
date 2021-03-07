# Компьютерный формат даты и времени обычно выглядит так: 21.05.2018 16:30
# Люди предпочитают видеть эту же информацию в более развернутом виде: 21 May 2018 year, 16 hours 30 minutes
# Ваша задача - преобразовать дату и время из числового формата и словесно-числовой.
#
# example
#
# Входные данные: Дата и время как строка, состоящая из чисел (например: 14.02.2018 16:55)
#
# Выходные данные: Та же самая дата и время, но в более развернутом формате
#
# Пример:
#
# date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# # Обратите внимание, что слова "hour" и "minute" (в единственном числе) используются только когда время 01:mm (1 hour)
# или hh:01 (1 minute).
# # Во всех остальных случаях следует использовать "hours" и "minutes".
# # Для названий месяцев и остальных слов следует использовать их английские эквиваленты -
# # January, February, March, April, May, June, July,
# # August, September, October, November, December;
# # year, hour/hours, minute/minutes


# Как это используется: Для улучшения взаимопонимания между человеком и компьютером.
#
# Предусловия:
# 0 < date <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 < hours < 24
# 0 < minutes < 60
import calendar
import datetime


def date_time(time: str) -> str:
    #replace this for solution
    format_str = "%d.%m.%Y %H:%M"
    datetime_obj = datetime.datetime.strptime(time, format_str)
    text_hour = ""
    text_min = ""

    day = datetime_obj.date().day
    month = calendar.month_name[datetime_obj.date().month]
    year = datetime_obj.date().year
    hour = datetime_obj.time().hour
    minute = datetime_obj.time().minute

    if datetime_obj.time().hour == 1:
        text_hour = "hour"
    else:
        text_hour = "hours"

    if datetime_obj.time().minute == 1:
        text_min = "minute"
    else:
        text_min = "minutes"

    return "{0} {1} {2} year {3} {4} {5} {6}".format(day, month, year, hour, text_hour, minute, text_min)

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
