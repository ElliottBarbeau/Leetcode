class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        d = {}
        a = sorted(arr)
        i = 0
        count = 0
        while i < len(a):
            if a[i] not in d:
                d[a[i]] = count + 1
                count += 1
            i += 1
            
        for i in range(len(arr)):
            arr[i] = d[arr[i]]
            
        return arr