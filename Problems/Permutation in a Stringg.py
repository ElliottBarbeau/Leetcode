class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        char_map = {}
        d = {}
        for char in s1:
            if char not in char_map:
                char_map[char] = 0
            char_map[char] += 1

        count = 0
        for window_end in range(len(s2)):
            count += 1
            if s2[window_end] not in d:
                d[s2[window_end]] = 0
            d[s2[window_end]] += 1

            if count > len(s1):
                d[s2[window_start]] -= 1
                if d[s2[window_start]] == 0:
                    del d[s2[window_start]]
                window_start += 1

            print(d, char_map)
            if d == char_map:
                return True

        return False

s1 = "ccc"
s2 = "cbac"
print(Solution().checkInclusion(s1, s2))
