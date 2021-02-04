class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        MAPPING = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0
        }
        s = str(n)
        prod = 1
        sm = 0
        for dig in s:
            prod *= MAPPING[dig]
            sm += MAPPING[dig]
        return prod - sm

print(Solution().subtractProductAndSum(23456))