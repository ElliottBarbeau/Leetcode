import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    left, right = find_searchable_bounds(0, 1, key, reader)
    while left <= right:
        middle = left + (right - left) // 2
        if reader.get(middle) == key:
            return middle
        elif reader.get(middle) > key:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def find_searchable_bounds(left, right, key, reader):
    left, right = left, right
    while reader.get(right) < key:
        newLeft = right + 1
        right += (right - left + 1) * 2
        left = newLeft
    return (left, right)


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()
