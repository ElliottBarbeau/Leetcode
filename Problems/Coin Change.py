class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        passed, failed = 1, 40000
        testing = 1
        while passed < failed:
            print(passed, failed)
            if self.subsetSum(testing, coins):
                passed = testing
                testing = (passed + failed) // 2
            else:
                failed = testing
                testing = (passed + failed) // 2
    
    
    def subsetSum(self, i, coins):
        subset = [[False for j in range(i + 1)] for a in range(len(coins) + 1)]
        for k in range(len(coins) + 1):
            subset[k][0] = True

        for l in range(1, i + 1):
            subset[0][l] = False

        for n in range(1, len(coins) + 1):
            for m in range(1, i + 1):
                if m < coins[n - 1]:
                    subset[n][m] = subset[n - 1][m]
                if m >= coins[n - 1]:
                    subset[n][m] = subset[n - 1][m-coins[n - 1]] or subset[n - 1][m]

        return subset[len(coins)][i]

print(Solution().getMaximumConsecutive([1,3]))