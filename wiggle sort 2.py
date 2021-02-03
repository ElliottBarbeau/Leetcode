class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = n // 2
        left, right = [], []
        for i in range(mid):
            left.append(nums[i])
            
        for i in range(mid, n):
            right.append(nums[i])
            
        print(left, right)
            
        l, r = 0, len(right) - 1
        res = []
        while l < len(left) and r >= 0:
            res.append(left[l])
            res.append(right[r])
            l += 1
            r -= 1
            
        return res
            
print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))