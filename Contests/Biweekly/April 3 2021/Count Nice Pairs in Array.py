class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        d = {}
        count = 0
        for i in range(len(nums)):
            nums[i] = nums[i] - self.rev(nums[i])
            if nums[i] not in d:
                d[nums[i]] = 0
            d[nums[i]] += 1
            
        for key in d:
            count += sum(x for x in range(d[key]))
            
        return count % (10**9 + 7)
        
    def rev(self, num):
        s = str(num)[::-1]
        s = s.lstrip("0") or 0
        return int(s)