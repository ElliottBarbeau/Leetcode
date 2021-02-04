def search_rotated_array(arr, key):
    rotation_point = find_rotation_point(arr)
    search_left_side = key > arr[0]
    return binary_search(arr, key, search_left_side, rotation_point)


def find_rotation_point(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] > arr[middle + 1]:
            return middle
        elif arr[middle - 1] > arr[middle]:
            return middle - 1
        if arr[left] > arr[middle]:
            right = middle
        elif arr[right] < arr[middle]:
            left = middle + 1

def binary_search(arr, key, search_left_side, rotation_point):
    if search_left_side:
        left, right = 0, rotation_point
    else:
        left, right = rotation_point, len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            right = middle - 1
        else:
            left = middle + 1

    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
