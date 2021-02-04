from heapq import *


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    left, right = index - K, index + K

    left = max(left, 0)
    right = min(right, len(arr) - 1)

    minHeap = []
    res = []

    for i in range(left, right + 1):
        heappush(minHeap, (-abs(X - arr[i]), arr[i]))
        if len(minHeap) > K:
            heappop(minHeap)

    while minHeap:
        res.append(heappop(minHeap)[1])

    return sorted(res)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return left if abs(left - target) < abs(target - right) else right


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
