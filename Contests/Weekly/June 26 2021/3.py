class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        window_start = 0
        count = 0
        d = {}
        odd_count = 0
        subc = 0
        for window_end in range(len(word)):
            while window_end < window_start:
                continue
            if word[window_end] not in d:
                d[word[window_end]] = 0
            d[word[window_end]] += 1

            if d[word[window_end]] % 2 != 0:
                odd_count += 1
            elif d[word[window_end]] > 1:
                odd_count -= 1

            print(odd_count)

            if odd_count > 1 or window_end == len(word) - 1:
                n = window_end - window_start - 2
                count += (n * (n + 1) / 2)
                while odd_count > 1:
                    d[window_start] -= 1
                    subc += 1
                    if d[window_start] % 2 == 0:
                        odd_count -= 1
                    window_start += 1
                
                count -= (subc * (subc + 1) / 2)
            

        return count

print(Solution().wonderfulSubstrings("aabb"))