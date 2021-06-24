class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        arr = arr[::-1]
        currLargest = -1
        for i in range(len(arr)):
            temp = arr[i]
            arr[i] = currLargest
            currLargest = max(currLargest, temp)
            
        return arr[::-1]