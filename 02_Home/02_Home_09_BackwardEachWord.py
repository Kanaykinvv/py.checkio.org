# В заданной строке вы должны перевернуть каждое слово, но слова должны оставаться на своих местах.
#
# Input: A string.
#
# Output: A string.
#
# Example:
#
# backward_string_by_word('') == ''
# backward_string_by_word('world') == 'dlrow'
# backward_string_by_word('hello world') == 'olleh dlrow'
# backward_string_by_word('hello   world') == 'olleh   dlrow'

# Предварительное условие: строка состоит только из буквенных символов и пробелов.
def backward_string_by_word(text: str) -> str:
    # your code here
    result = ""
    if len(text) > 0:
        list_words = text.split(" ")
        for word in range(0, len(list_words)):
            if list_words[word] == "":
                result += " "
            else:
                if word != (len(list_words) - 1):
                    result += list_words[word][::-1] + " "
                else:
                    result += list_words[word][::-1]
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
