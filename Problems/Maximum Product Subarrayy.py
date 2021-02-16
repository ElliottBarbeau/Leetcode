class Solution:
    def maxProduct(self, nums) -> int:
        maxx, minn, result = 1, 1, float('-inf')
        for num in nums:
            a = maxx * num
            b = minn * num
            maxx = max(a, b, num)
            minn = min(a, b, num)
            result = max(result, maxx)

        return result if result != float('inf') else 0

print(Solution().maxProduct([2, 3, -1, 4]))
