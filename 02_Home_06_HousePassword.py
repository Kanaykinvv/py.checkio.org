# Стефан и София забывают о безопасности и используют простые пароли для всего. Помогите Николе разработать модуль для
# проверки паролей на безопасность. Пароль считается достаточно стойким, если его длина больше или равна 10 символам,
# он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только
# латинские буквы и/или цифры.
#
# Вх. данные: Пароль как строка.
#
# Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть
# сконвертирован и представлен как булево значение (True или False)
#
# Пример:
#
# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True

#
# Как это используется: Если вы беспокоитесь о безопасности вашего приложения или сервиса, вы можете проверять
# пароли ваших пользователей на "сложность". Также вы можете использовать свои навыки и усложнить требования к паролям.
#
# Предусловия:
# re.match("[a-zA-Z0-9]+", password)
# 0 < len(password) ≤ 64
import re


def checkio(data: str) -> bool:
    if re.search(r'[A-Z]{1}', data) and re.search(r'[a-z]{1}', data) and re.search(r'[0-9]{1}', data) and len(data) >=10:
        return True
    else:
        return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")