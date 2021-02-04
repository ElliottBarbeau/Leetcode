def count_rotations(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2

        if middle < right and arr[middle] > arr[middle + 1]:
            return middle + 1
        elif middle > left and arr[middle - 1] > arr[middle]:
            return middle

        if arr[left] < arr[middle]:
            left = middle + 1
        elif arr[right] > arr[middle]:
            right = middle - 1

    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
