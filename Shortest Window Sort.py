def shortest_window_sort(arr):
    left, right = 0, 0

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            left = i+1
            break

    for i in reversed(range(1, len(arr))):
        if arr[i] < arr[i-1]:
            right = i-1
            break

    if left == right == 0:
        return 0

    subarray = arr[left : right + 1]
    max_sub = max(subarray)
    min_sub = min(subarray)

    for i in reversed(range(left)):
        if arr[i] > min_sub:
            left -= (left - i)

    for i in range(right, len(arr)):
        if arr[i] < max_sub:
            right += (i - right)

    return right - left + 1

print(shortest_window_sort([3, 2, 1]))