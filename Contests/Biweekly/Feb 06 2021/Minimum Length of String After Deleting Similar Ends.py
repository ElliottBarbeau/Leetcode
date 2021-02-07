class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while len(s) > 0 and s[left] == s[right] and left < right:
            while left < right and s[left] == s[left + 1]:
                left += 1
                
            while left < right and s[right] == s[right - 1]:
                right -= 1
                
            s = s[left + 1 : right]
            left, right = 0, len(s) - 1
            
        return len(s)

print(Solution().minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"))
print(Solution().minimumLength("cabaabac"))
print(Solution().minimumLength("aabccabba"))
print(Solution().minimumLength("ca"))