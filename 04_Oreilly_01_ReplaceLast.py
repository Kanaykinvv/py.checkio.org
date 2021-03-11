# В данном списке последний элемент должен стать первым. Пустой список или список только с одним элементом
# должны оставаться неизменными.
# Input: List.
#
# Output: Iterable.
#
# Example:
#
# replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
# replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
# replace_last([1]) == [1]
# replace_last([]) == []
def replace_last(line: list) -> list:
    # your code here
    if (len(line) == 0) or (len(line) == 1):
        return line

    for n in range(len(line)-1, 0, -1):
        line[n], line[n-1] = line[n-1], line[n]

    return line



if __name__ == '__main__':
    print("Example:")
    print(replace_last([2, 3, 4, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
    assert replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
    assert replace_last([1]) == [1]
    assert replace_last([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
