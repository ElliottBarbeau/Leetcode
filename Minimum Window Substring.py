class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, curr_length, ans = 0, 0, float('inf'), ''
        t_count = {}
        window_count = {}
        formed = 0

        for char in t:
            if char not in t_count:
                t_count[char] = 1
            else:
                t_count[char] += 1

        required = len(t_count)
        while r < len(s):
            if s[r] not in window_count:
                window_count[s[r]] = 1
            else:
                window_count[s[r]] += 1

            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                formed += 1
        
            while l <= r and formed == required:
                if r - l + 1 < curr_length:
                    ans = s[l : r + 1]
                    curr_length = r - l + 1

                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    formed -= 1

                l += 1
        
            r += 1
        return ans
            


print(Solution().minWindow('ab', 'b'))