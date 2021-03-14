from collections import defaultdict
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d = defaultdict(list)
        total = 0
        for i in range(len(s1)):
            d[s1[i]].append(i)
            
        for j in range(len(s2)):
            if s2[j] not in d:
                return False
            if j not in d[s2[j]]:
                total += 1
                
        return (total == 0 or total == 2)