class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i:len(needle)+i] == needle:
                return i

        return -1


print(Solution().strStr('hello', 'll'))