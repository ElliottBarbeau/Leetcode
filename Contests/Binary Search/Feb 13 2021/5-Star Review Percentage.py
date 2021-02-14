class Solution:
    def solve(self, reviews, threshold):
        five_star = 0
        total = 0
        for review in reviews:
            five_star += review[0]
            total += review[1]
        num = 0
        while (five_star/total) * 100 < threshold:
            five_star += 1
            total += 1
            num += 1

        return num