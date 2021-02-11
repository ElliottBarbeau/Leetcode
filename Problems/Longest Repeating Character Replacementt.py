class Solution:
    def characterReplacement(self, s, k) -> int:
        d = {}
        max_repeating_character, max_length, curr_length = 0, 0, 0
        window_start = 0
        for window_end in range(len(s)):
            curr_length += 1
            if s[window_end] not in d:
                d[s[window_end]] = 0
            d[s[window_end]] += 1

            max_repeating_character = max(max_repeating_character, d[s[window_end]])
            while curr_length - max_repeating_character > k:
                d[s[window_start]] -= 1
                window_start += 1
                curr_length -= 1

            max_length = max(max_length, curr_length)

        return max_length

print(Solution().characterReplacement("AABABBA", 1))