def search_min_diff_element(arr, key):
    left, right = 0, len(arr) - 1
    if key < arr[0]:
        return arr[0]
    n = len(arr)
    if key > arr[n - 1]:
        return arr[n - 1]

    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return arr[middle]
        elif arr[middle] < key:
            left = middle + 1
        else:
            right = middle - 1
    if (arr[left] - key) < (key - arr[right]):
        return arr[left]
    return arr[right]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
