#Brute force
#Time complexity: O(N^2)
#Space complexity: O(1) -> this is outweighed by awful time complexity
class Solution1:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num + num2 == target and i != j:
                    return [i, j]

#Two pass dictionary approach
#Time complexity: O(2N) == O(N)
#Space complexity: O(N) -> dictionary is worst case same size as # of integers in nums
class Solution2:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in d and d[target-nums[i]] != i:
                return [d[target-nums[i]], i]

#One pass dictionary approach
#Time complexity: O(N)
#Space complexity: O(N) -> dictionary is worst case same size as # of integers in nums
class Solution3:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            else:
                d[nums[i]] = i

#Left and right pointer approach
#Time complexity: O(NlogN)
#Space complexity: O(1)
#Trades off logN runtime for constant space
#This algorithm only works for the questions that ask for the numbers rather than the index
class Solution4:
    def twoSum(self, nums, target):
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return [nums[left], nums[right]]