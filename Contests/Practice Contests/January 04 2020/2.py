class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        res = 0
        for i in arr:
            res ^= i
            ans.append(res)
        
        new = []
        for i,j in queries:
            if not i:
                new.append(ans[j])
            else:
                new.append(ans[j] ^ ans[i-1])
        return new