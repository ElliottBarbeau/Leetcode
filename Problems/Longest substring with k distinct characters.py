class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
        d = {}
        windowStart = 0

        max_length = float('-inf')

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in d:
                d[right_char] = 0
            d[right_char] += 1

            while len(d) > k:
                left_char = s[windowStart]
                d[left_char] -= 1
                if d[left_char] == 0:
                    del d[left_char]
                windowStart += 1

            max_length = max(max_length, window_end - windowStart + 1)
        return 0 if max_length == float('-inf') else max_length

print(Solution().lengthOfLongestSubstringKDistinct('abcabcabc', 2))