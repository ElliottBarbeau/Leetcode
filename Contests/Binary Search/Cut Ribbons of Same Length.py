class Solution:
    def solve(self, ribbons, k):
        max_length = max(ribbons)
        left, right = 1, max_length
        while left < right - 1:
            mid = left + (right - left) // 2
            if self.helper(ribbons, mid, k):
                left = mid
            else:
                right = mid - 1
        if self.helper(ribbons, right, k):
            return right
        elif self.helper(ribbons, left, k):
            return left
        else:
            return -1
        
    def helper(self, ribbons, length, k):
        p = 0
        for r in ribbons:
            p += r // length
        if p >= k:
            return True
        else:
            return False

ribbons = [1]
k = 2
print(Solution().solve(ribbons, k))