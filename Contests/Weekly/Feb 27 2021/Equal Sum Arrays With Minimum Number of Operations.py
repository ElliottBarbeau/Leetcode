from copy import *
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 == s2:
            return 0
        if s1 < s2:
            temp = deepcopy(nums1)
            nums1 = deepcopy(nums2)
            nums2 = deepcopy(temp)
            temp2 = s2
            s2 = s1
            s1 = temp2

        nums1.sort()
        nums1 = nums1[::-1]
        nums2.sort()
        n1s = len(nums1)
        n2s = len(nums2)

        count = 0
        index_n1 = 0
        index_n2 = 0
        first, second = 0, 0
        while s1 > s2:
            if index_n1 < n1s:
                first = nums1[index_n1]
            else:
                first = 1

            if index_n2 < n2s:
                second = nums2[index_n2]
            else:
                second = 6

            if first == 1 and second == 6:
                break

            count += 1

            if first - 1 > 6 - second:
                index_n1 += 1
                s1 += 1 - first
            else:
                index_n2 += 1
                s2 += 6 - second

        if s1 > s2:
            count = -1
        return count

nums1 = [5,6,4,3,1,2]
nums2 = [6,3,3,1,4,5,3,4,1,3,4]
print(Solution().minOperations(nums1, nums2))
                    