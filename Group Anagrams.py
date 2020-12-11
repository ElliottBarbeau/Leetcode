class Solution:
    def groupAnagrams(self, strs):
        d = {}
        res = []
        for s in strs:
            if "".join(sorted(s)) not in d:
                d["".join(sorted(s))] = [s]
            else:
                d["".join(sorted(s))].append(s)
        for key in d.keys():
            res.append(d[key])
            
        return res

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))