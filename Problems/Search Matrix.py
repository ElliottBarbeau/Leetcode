class Solution:
    def searchMatrix(self, matrix, target):
        for m in matrix:
            print(m)
            last_element = m[-1]
            if last_element == target:
                return True
            elif last_element > target:
                arr = m
                break
                
        left, right = 0, len(arr) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if arr[middle] == target:
                return True
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))