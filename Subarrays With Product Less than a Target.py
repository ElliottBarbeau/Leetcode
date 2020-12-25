from collections import deque

'''
def find_subarrays(arr, target):
    result = []
    curr_product = 1

    window_start = 0
    n = len(arr)

    for window_end in range(n):
        curr_product *= arr[window_end]
        while (curr_product >= target):
            curr_product /= arr[window_start]
            window_start += 1

        temp_list = deque()
        for i in range(window_end, window_start-1, -1):
            temp_list.appendleft(arr[i])
            result.append(list(temp_list))
    return result
'''

def find_subarrays(arr, target):
    result = []
    curr_product = 1

    window_start = 0
    n = len(arr)

    for window_end in range(n):
        if arr[window_end] < target:
            result.append([arr[window_end]])
        
        curr_product *= arr[window_end]

        while curr_product >= target:
            curr_product /= arr[window_start]
            window_start += 1

        if curr_product < target and arr[window_start : window_end + 1] not in result:
            result.append(arr[window_start : window_end + 1])

    return result
print(find_subarrays([2, 5, 3, 10], 30))