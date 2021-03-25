# В этой миссии Вам надо определить, все ли элементы массива равны.
#
# Входные: List.
#
# Выходные: Bool.
#
# Примеры:
#
# all_the_same([1, 1, 1]) == True
# all_the_same([1, 2, 1]) == False
# all_the_same(['a', 'a', 'a']) == True
# all_the_same([]) == True

# Precondition: all elements of the input list are hashable
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if len(elements) <= 1:
        return True
    else:
        for i in range(1, len(elements)):
            if elements[i - 1] != elements[i]:
                return False
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
