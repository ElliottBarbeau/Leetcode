class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        not_holding = 0
        not_holding_cooldown = float('-inf')
        hold = float('-inf')

        for price in prices:
            hold, not_holding, not_holding_cooldown = max(hold, not_holding - price), max(not_holding, not_holding_cooldown), hold + price

        return max(not_holding_cooldown, not_holding)