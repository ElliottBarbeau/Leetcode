class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in d and t[i] not in d.values():
                d[s[i]] = t[i]
            elif s[i] in d and t[i] == d[s[i]]:
                continue
            else:
                return False

        return True

print(Solution().isIsomorphic('ab', 'aa'))