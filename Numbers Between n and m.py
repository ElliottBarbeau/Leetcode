#You are given a sorted array and two different numbers, n and m. There may be duplicates in the array.
#You have to answer the number of elements that are greater than n and less than m.

def numbers_between_n_and_m(arr, n, m):
    first_index = binary_search(arr, m, True)
    last_index = binary_search(arr, n, False)
    return first_index - last_index - 1
    
def binary_search(arr, target, find_first):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            key_index = middle
            if find_first:
                right = middle - 1
            else:
                left = middle + 1

    return key_index

print(numbers_between_n_and_m([1, 3, 3, 3, 8, 8, 8, 8, 10, 15], 3, 15))