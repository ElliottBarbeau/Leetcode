class Solution:
    def printVertically(self, s: str) -> list[str]:
        check = s.split(" ")
        i = 0
        longest = float('-inf')
        for word in check:
            longest = max(longest, len(word))
            
        ans = ["" for _ in range(longest)]
            
        for i in range(len(check)):
            for j in range(longest):
                if j >= len(check[i]):
                    ans[j] += (" ")
                else:
                    ans[j] += (check[i][j])
        
        for i in range(len(ans)):
            ans[i] = ans[i].rstrip()
            
        return ans