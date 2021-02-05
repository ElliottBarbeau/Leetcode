from heapq import *
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        maxheap = []
        ret = []
        for i in range(len(nums1)):
            if maxheap and nums1[i] > -maxheap[0][0]: continue
            for j in range(len(nums2)):
                if maxheap and nums2[j] > -maxheap[0][0]: continue
                s = nums1[i] + nums2[j]
                if len(maxheap) < k:
                    heappush(maxheap, (-s, [nums1[i], nums2[j]]))
                else:
                    if s < -maxheap[0][0]:
                        heappushpop(maxheap, (-s, [nums1[i], nums2[j]]))
        

        while maxheap:
            ret.append(heappop(maxheap)[1])

        return ret

print(Solution().kSmallestPairs([1,2], [3], 3))