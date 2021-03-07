from heapq import nlargest
class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        '''
        Didn't finish this one in time, should come back to it eventually
        '''
        if len(nums) == 1:
            return 0 if nums[0] == 0 else 1

        d = {}
        new = []
        for i in range(0, len(nums), k):
            new.append(nums[i:i + k])

        for sub in new:
            seen = set()
            for num in sub:
                if num not in seen:
                    if num not in d:
                        d[num] = 0
                    d[num] += 1
                    seen.add(num)
                    
        if k == 1:
            if 0 in d:
                return len(nums) - d[0]
            else:
                return len(nums)
        
        index_no_change = set()
        largest_vals = nlargest(k, d, key=d.__getitem__)
        new_largest_vals = []
        for i in range(len(largest_vals)):
            if d[largest_vals[i]] != 1:
                new_largest_vals.append(largest_vals[i])
        for i in range(len(nums)):
            curr = nums[i : i + k]
            l = set(curr).intersection(set(new_largest_vals))
            if len(l) > 1:
                for j in range(len(curr)):
                    if curr[j] in new_largest_vals:
                        index_no_change.add(i + j)
        print(index_no_change)
        return len(nums) - len(index_no_change)


nums = [1, 2, 3, 1, 2, 5, 1, 2, 6]
k = 3
print(Solution().minChanges(nums, k))

# nums = [0]
# k = 1
# print(Solution().minChanges(nums, k))

# nums = [23,27,14,0,14,3,7,10,14,23,5,5]
# k = 1
# print(Solution().minChanges(nums, k))

# nums = [26,19,19,28,13,14,6,25,28,19,0,15,25,11]
# k = 3
# print(Solution().minChanges(nums, k))

# nums = [16,5,15,6,1,25,0,13,12,12,7,16,4,25,3]
# k = 3
# print(Solution().minChanges(nums, k))

# nums = [1,2,4,1,2,5,1,2,6]
# k = 3
# print(Solution().minChanges(nums, k))

# nums = [11,20,3,18,26,30,20,7,3,0,25,9,19,21,3,23]
# k = 5
# print(Solution().minChanges(nums, k))