class Solution:
    '''
    doesnt quite work
    '''
    def maximumScore(self, nums: list[int], k: int) -> int:
        ret = [nums[k]]
        curr_max = float('-inf')
        m = float('inf')
        left, right = k - 1, k + 1
        while left >= 0 and right < len(nums):
            print(ret, left, right)
            if left > 0 and nums[left] > nums[right]:
                ret.append(nums[left])
                m = min(m, nums[left])
                left -= 1
                
            elif right <= len(nums) - 1 and nums[right] >= nums[left]:
                ret.append(nums[right])
                m = min(m, nums[right])
                right += 1
                
            curr_max = max(len(ret) * m, curr_max)

        if right == len(nums):
            while left >= 0:
                ret.append(nums[left])
                m = min(m, nums[left])
                left -= 1
                
            curr_max = max(len(ret) * m, curr_max)

        if left == -1:
            while right < len(nums):
                ret.append(nums[right])
                m = min(m, nums[right])
                right += 1
                
            curr_max = max(len(ret) * m, curr_max)
            
        return curr_max
        
nums = [1,4,3,7,4,5]
k = 3
print(Solution().maximumScore(nums, k))