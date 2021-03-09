# Ваша задача - расшифровать сообщение используя азбуку Морзе.
# В шифровке будет использован 1 пробел между буквами одого слова и 3 пробела между отдельными словами.
# Если расшифрованный текст начинается со слова, первая буква этого слова должна быть заглавной.
#
# example
#
# Входные данные: Секретное сообщение
#
# Выходные данные: Расшифрованный текст
#
# Примеры:
#
# morse_decoder("... --- -- .   - . -..- -") == "Some text"
# morse_decoder("..--- ----- .---- ---..") == "2018"
# morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

# Как это используется: Для криптографии, передачи и защиты важной информации.
#
# Предусловия:
# 0 < len(message) < 100
# Текст будет состоять только из цифр и букв английского алфавита.
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    #replace this for solution
    words = code.split("   ")
    result = ""

    for word in words:
        for char in word.split(" "):
            result += MORSE[char]
        result += " "

    if len(result) > 0:
        result = result[:1].upper() + result[1:].rstrip()

    return result

if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))


    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")
