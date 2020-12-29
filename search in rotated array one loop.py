def search_rotated_array(arr, key):
    left, right = 0, len(arr)-1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return middle
        if arr[left] <= arr[middle]:
            if key > arr[left] and key < arr[middle]:
                right = middle - 1
            else:
                left = middle +1
        else:
            if key < arr[right] and key > arr[middle]:
                left = middle + 1
            else:
                right = middle - 1
        
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
