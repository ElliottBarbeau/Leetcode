def search_bitonic_array(arr, key):
    max_index = find_max_point(arr)
    left_search = binary_search(arr, key, 0, max_index, True)
    if left_search != -1:
        return left_search
    return binary_search(arr, key, max_index, len(arr) - 1, False)

def find_max_point(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle

    return left

def binary_search(arr, key, left, right, increasing):
    left, right = left, right
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return middle
        if increasing:
            if arr[middle] < key:
                left = middle + 1
            else:
                right = middle - 1
        else:
            if arr[middle] < key:
                right = middle - 1
            else:
                left = middle + 1

    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
