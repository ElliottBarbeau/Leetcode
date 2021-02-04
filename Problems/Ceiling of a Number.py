def search_ceiling_of_a_number(arr, key):
    left, right = 0, len(arr) - 1
    if key > arr[right]:
        return -1

    while left <= right:
        middle = left + (right - left) // 2
        if key < arr[middle]:
            right = middle - 1
        elif key > arr[middle]:
            left = middle + 1
        else:
            return middle
        
    return left


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
