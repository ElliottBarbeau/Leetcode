class Solution:
    def climbStairs(self, n):
        a, m = 1, 1
        for _ in range(n):
            a, m = m, a + m
        return a

print(Solution().climbStairs(3))