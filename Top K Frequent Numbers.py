from heapq import *

def find_k_frequent_numbers(nums, k):
    seen = {}
    minHeap = []
    res = []

    for i in range(k):
        num = nums[i]
        if num not in seen:
            seen[num] = 0
        seen[num] += 1
        heappush(minHeap, (seen[num], num))

    for i in range(k, len(nums)):
        num = nums[i]
        if num not in seen:
            seen[num] = 0
        seen[num] += 1

        if seen[num] > minHeap[0][0]:
            heappop(minHeap)
            heappush(minHeap, (seen[num], num))

    print(seen)
    print(minHeap)

    while minHeap:
        res.append(heappop(minHeap)[1])

    return res


def main():
    print((find_k_frequent_numbers([5, 12, 11, 3, 11, 11, 3, 5, 8, 9, 10, 10, 9, 8, 8, 9, 8], 2)))


main()
