class Solution:
    def waysToSplit(self, nums):
        n = len(nums)
        pre, post = [0] * n, [0] * n
        pre[0] = nums[0]
        post[n-1] = nums[n-1]

        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i]

        for i in reversed(range(n-1)):
            post[i] = post[i+1] + nums[i]

        start, end = 1, 1
        current_sum, res = 0, 0

        while start < n - 1 and end < n - 1:
            while current_sum < pre[start - 1] and end < n - 1:
                current_sum += nums[end]
                end += 1

            if current_sum <= post[end]:
                res += 1

            current_sum -= nums[start]
            start += 1

        return res

print(Solution().waysToSplit([1,2,2,2,5,0]))