class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        ans = set()
        
        for i in range(1, (n // 2) + 1):
            for left in range(n - 2 * i + 1):
                mid = left + i
                right = mid + i
                ls = text[left : mid]
                rs = text[mid : right]
                if ls == rs:
                    ans.add(ls)
                    
        return len(ans)