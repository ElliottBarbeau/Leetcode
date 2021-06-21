class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        s = [[0] * n for _ in range(m)]
        
        for i in range(m):
            prefix = 0
            for j in range(n):
                prefix += mat[i][j]
                s[i][j] = prefix
                
        ret = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                l = 0
                if i - k > 0:
                    l = i - k
                    
                h = m - 1
                if i + k < m - 1:
                    h = i + k
                    
                prefix = 0
                for r in range(l, h + 1):
                    hp = min(n - 1, j + k)
                    lp = j - k - 1
                    if lp < 0:
                        prefix += s[r][hp]
                    else:
                        prefix += s[r][hp] - s[r][lp]
                        
                ret[i][j] = prefix
                
        return ret