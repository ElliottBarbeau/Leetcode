def binary_search(arr, key):
    left_to_right = arr[0] < arr[-1]
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return middle
        
        if left_to_right:
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
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
