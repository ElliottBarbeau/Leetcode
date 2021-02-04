def find_max_in_bitonic_array(arr):
    # TODO: Write your code here
    left, right = 0, len(arr) - 1

    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] < arr[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return arr[left]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
