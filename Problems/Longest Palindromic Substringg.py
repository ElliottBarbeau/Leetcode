class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_right = 0
        res_left = 0
        res_len = 0
        
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_right = right
                    res_left = left
                    res_len = right - left + 1
                left -= 1
                right += 1
            
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > res_len:
                    res_right = right
                    res_left = left
                    res_len = right - left + 1
                left -= 1
                right += 1
                    
        return s[res_left : res_right + 1]