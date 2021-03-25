# Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.
#
# Это упрощенная версия миссии Between Markers.
#
# Начальный и конечный маркеры всегда разные.
# Начальный и конечный маркеры всегда размером в один символ.
# Начальный и конечный маркеры всегда есть в строке и идут один за другим.
# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
#
# Output: Строка.
#
# Пример:
#
# between_markers('What is >apple<', '>', '<') == 'apple'
# 1
# Как это используется: Может использоваться для парсинга небольшой верстки.
#
# Предусловия: Не может быть более одного маркера одного типа.
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    return text[text.find(begin) + 1:text.find(end)]

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
