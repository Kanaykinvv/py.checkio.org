# Create and return a new iterable that contains the same elements as the argument iterable items, but with the
# reversed order of the elements inside every maximal strictly ascending sublist. This function should not modify
# the contents of the original iterable.
#
# Input: Iterable
#
# Output: Iterable
#
# Example:
#
# reverse_ascending([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
# reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
# How it is used: (math is used everywhere)
#
# Precondition: Iterable contains only ints
# def reverse_ascending(items):
#     print("-"*50)
#     print(items)
#
#     for i in range(len(items)):
#         for index in range(len(items)-1):
#             if items[index] < items[index+1]:
#                 items[index], items[index + 1] = items[index + 1], items[index]
#
#     print(items)
#     return items

def reverse_ascending(items):
    print("-"*50)
    res = []
    start = 0
    print(items)
    for i in range(1, len(items)):
        print("i = " + str(i))
        if items[i] <= items[i-1]:
            print("items[i] <= items[i-1] : items[" + str(i) + "] (" + str(items[i]) +") <= items[" + str(i-1) + "] (" + str(items[i - 1]) +")" )
            print("res = res + items[start:i][::-1]")
            res = res + items[start:i][::-1]
            print(res)
            start = i
            print("start = i = " + str(i))
        else:
            print("items[i] > items[i-1] : items[" + str(i) + "] (" + str(items[i]) +") > items[" + str(i-1) + "] (" + str(items[i - 1]) +")" )
    finall = res+items[start:][::-1]
    print("res+items[start:][::-1]")
    print(finall)
    return finall

if __name__ == '__main__':
    print("Example:")
    # print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
