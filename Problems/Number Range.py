def find_range(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            while arr[left] < key:
                left += 1
            while arr[right] > key:
                right -= 1
            return [left, right]
        elif arr[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

    return [-1, -1]


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
