class Solution:
    def maxAbsoluteSum(self, nums) -> int:
        if not nums:
            return
        minhere, maxhere = float('inf'), float('-inf')
        minsofar, maxsofar = float('inf'), float('-inf')
        
        for i in range(len(nums)):
            if minhere > 0:
                minhere = nums[i]
            else:
                minhere += nums[i]

            if maxhere < 0:
                maxhere = nums[i]
            else:
                maxhere += nums[i]

            minsofar = min(minsofar, minhere)
            maxsofar = max(maxsofar, maxhere)
            
        return max(abs(minsofar), maxsofar)

print(Solution().maxAbsoluteSum([1,-3,2,3,-4]))
print(Solution().maxAbsoluteSum([2,-5,1,-4,3,-2]))
print(Solution().maxAbsoluteSum([1]))
print(Solution().maxAbsoluteSum([1,-3,2,3,-4,5,-10]))
print(Solution().maxAbsoluteSum([-3,-5,-3,-2,-6,3,10,-10,-8,-3]))
