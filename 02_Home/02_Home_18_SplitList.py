# You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should
# have more elements. If it has no elements, then two empty arrays should be returned.

# Вы должны разбить данный массив на два массива. Если в нем нечетное количество элементов, то в первом массиве
# должно быть больше элементов. Если в нем нет элементов, должны быть возвращены два пустых массива.

# Input: Array.
#
# Output: Array or two arrays.
#
# Example:
#
# split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
# split_list([1, 2, 3]) == [[1, 2], [3]]
def split_list(items: list) -> list:
    # your code here
    result = list()
    list_1 = list()
    list_2 = list()
    if len(items) > 0:
        if len(items) % 2 == 0:
            for i in range(0, len(items)//2):
                list_1.append(items[i])
            for i in range(len(items)//2, len(items)):
                list_2.append(items[i])
        else:
            for i in range(0, (len(items)//2) + 1):
                list_1.append(items[i])
            for i in range((len(items)//2) + 1, len(items)):
                list_2.append(items[i])
    result.append(list_1)
    result.append(list_2)
    return result

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6, 7]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
