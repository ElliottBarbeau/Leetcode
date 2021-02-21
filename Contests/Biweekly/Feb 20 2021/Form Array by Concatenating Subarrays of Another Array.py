class Solution:
    def canChoose(self, groups, nums) -> bool:
        last_seen = 0
        count = 0
        for group in groups:
            for i in range(last_seen, len(nums)):
                if nums[i : i + len(group)] == group:
                    count += 1
                    last_seen = i + len(group)
                    break
                
        return count == len(groups)

groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]

print(Solution().canChoose(groups, nums))