class Solution:
    def totalFruit(self, tree) -> int:
        d = {}
        window_start = 0
        total = 0
        max_total = -1
        for window_end in range(len(tree)):
            total += 1
            if tree[window_end] not in d:
                d[tree[window_end]] = 0
            d[tree[window_end]] += 1

            while len(d) > 2:
                d[tree[window_start]] -= 1
                if d[tree[window_start]] == 0:
                    del d[tree[window_start]]
                window_start += 1
                total -= 1
                
            max_total = max(max_total, total)

        return max_total


print(Solution().totalFruit([1,2,1]))
print(Solution().totalFruit([1,2,3,2,2]))
