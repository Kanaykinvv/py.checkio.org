# # Дан словарь, в котором в качестве ключей используются строки, а в качестве значений строки или словари.
# # Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах. Результатом будет словарь без
# # вложенных словарей. Ключи должны содержать путь, составленный из родительских ключей из начального словаря,
# # разделенных "/". Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой ("").
# # Взглянем на пример:
#
# {
#     "name": {
#         "first": "One",
#         "last": "Drone"
#     },
#     "job": "scout",
#     "recent": {},
#     "additional": {
#         "place": {
#             "zone": "1",
#             "cell": "2"}
#     }
# }
#
# Результатом будет:
#
# {"name/first": "One",           #один прародитель
#  "name/last": "Drone",
#  "job": "scout",                #ключ корневого уровня
#  "recent": "",                  #пустой словарь
#  "additional/place/zone": "1",  #третий уровень
#  "additional/place/cell": "2"}

# Входные данные: Оригинальный словарь (dict).
#
# Выходные данные: "Плоский" словарь (dict).
#
# Примеры:

# flatten({"key": "value"}) == {"key": "value"}
# flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
# flatten({"empty": {}}) == {"empty": ""}
#
# Связь с реальной жизнью: Методы из этой задачи будут полезны, чтобы разобрать и упростить структуры
# конфигураций или файлов. Вы легко можете улучшить данную концепцию для ваших конкретных задач.
# А также, чтение чужого кода и поиск ошибок - это очень полезный навык.
#
# Предусловия:
# Ключи в словаре - не пустые строки.
# Значения в словаре - строки или другие словари.
# root_dictionary != {}

def flatten(dictionary):
    result = dict()

    if len(dictionary) == 0:
        result[None] = ""
    else:
        for key, value in dictionary.items():
            print("-"*50)
            print("На входе ключ: " + str(key))
            print("На входе значение: " + str(value))
            if type(value) == dict:
                print("Значение это словарь")
                tmp_dict = flatten(value)
                for key2, value2 in tmp_dict.items():
                    key = key + "/" + key2
                    result[key] = value2
            else:
                print("Значение это строка -> минимальный словарь: " + str(key) + ":" + str(value))
                result[key] = value
            print("-"*50)
        print("end flatten | result = " + str(result))
    return result


if __name__ == '__main__':
    # test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    # print(' Input: {}'.format(test_input))
    # print('Output: {}'.format(flatten(test_input)))

    test_input = {
        # "key1": "value1", "key21": {"key22": "value2"}, "key31": {"key32": {"key33": "value3"}}
        "key1": {}
    }
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    # assert flatten(
    #     {"key": {"deeper": {"more": {"enough": "value"}}}}
    # ) == {"key/deeper/more/enough": "value"}, "Nested"
    # assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    # assert flatten({"name": {
    #                     "first": "One",
    #                     "last": "Drone"},
    #                 "job": "scout",
    #                 "recent": {},
    #                 "additional": {
    #                     "place": {
    #                         "zone": "1",
    #                         "cell": "2"}}}
    # ) == {"name/first": "One",
    #       "name/last": "Drone",
    #       "job": "scout",
    #       "recent": "",
    #       "additional/place/zone": "1",
    #       "additional/place/cell": "2"}
    # print('You all set. Click "Check" now!')
