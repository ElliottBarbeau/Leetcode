class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        d = {}
        max_length = 0
        for window_end in range(len(s)):
            if s[window_end] not in d:
                d[s[window_end]] = 1
            else:
                d[s[window_end]] += 1
                while d[s[window_end]] > 1:
                    d[s[window_start]] -= 1
                    window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

print(Solution().lengthOfLongestSubstring(""))