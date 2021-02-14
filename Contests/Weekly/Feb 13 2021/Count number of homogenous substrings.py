class Solution:
    def countHomogenous(self, s: str) -> int:
        d = {}
        window_start = 0
        count = 0
        for window_end in range(len(s)):
            if s[window_end] not in d:
                d[s[window_end]] = 0
            d[s[window_end]] += 1
            
            while len(d) > 1:
                d[s[window_start]] -= 1
                if d[s[window_start]] == 0:
                    del d[s[window_start]]
                window_start += 1
            
            if len(d) == 1:
                count += 1 * d[s[window_end]]
                
        return count % (10**9 + 7)

print(Solution().countHomogenous('z'))