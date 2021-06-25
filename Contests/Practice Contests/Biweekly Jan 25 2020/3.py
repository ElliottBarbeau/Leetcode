from collections import defaultdict
class Solution:
    def diagonalSort(self, m: list[list[int]]) -> list[list[int]]:
        d = defaultdict(list)
        
        for i in range(len(m)):
            for j in range(len(m[0])):
                d[i - j].append(m[i][j])
                
        for key in d.keys():
            d[key].sort()
            
        for i in range(len(m)):
            for j in range(len(m[0])):
                m[i][j] = d[i-j].pop(0)
                
        return m