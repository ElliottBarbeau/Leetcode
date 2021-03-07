from itertools import combinations
class Solution:
    def beautySum(self, s: str) -> int:
        if not s:
            return 0
        sub = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]
        total = 0
        
        for s in sub:
            if len(s) == 1:
                d = {}
                i = 0
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
            i += 1
            
            least_freq = min(d, key = d.get)
            most_freq = max(d, key = d.get)
                    
            total += d[most_freq] - d[least_freq]
            
        return total