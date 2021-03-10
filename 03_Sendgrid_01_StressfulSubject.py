# Функция должна распознавать является ли тема письма стрессовой. Стрессовая тема определяется тем, что все
# буквы в верхнем регистре, и / или заканчиваются как минимум тремя восклицательными знаками, и / или содержат
# по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent". Любое из этих слов-маркеров может
# быть написано по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень
# непринужденно «HHHEEEEEEEEELLP».
#
# Входные данные: Тема письма в виде строки.
#
# Выходные данные: Boolean.
#
# Пример:
#
# is_stressful("Hi") == False
# is_stressful("I neeed HELP") == True
# Предварительное условие: Тема может содержать до 100 букв.
import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    if subj.isupper():
        return True

    if subj[-3:] == "!!!":
        return True

    subj = subj.replace(" ", "").replace("!", "").replace("-", "").replace(".", "").lower()
    match = re.search(r'([h]+[e]+[l]+[p]+)|([a]+[s]+[a]+[p]+)|([u]+[r]+[g]+[e]+[n]+[t]+)', subj)

    return True if match else False




if __name__ == '__main__':
#     #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')
