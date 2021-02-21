from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    del_items = 0
    print("current items = " + str(items))
    print("current border = " + str(border))
    print("============")
    if len(items) != 0 and border in items:
        for position in range(len(items)):
            position -= del_items
            print("position = " + str(position))
            print("items = " + str(items))
            if items[position] != border:
                print("items[position] != border")
                del items[position]
                print("del items[position] -> " + "items = " + str(items))
                del_items += 1
                print("del_items += 1 -> del_items = " + str(del_items))
            else:
                print("items[position] == border break")
                break
            print("======== end circle ========")
    else:
        print("len(items) = 0 or border not in items")
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
