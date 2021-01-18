from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = i = 0

        for j,sell in enumerate(prices):
            best = max(best, sell-prices[i])
            i = j if sell < prices[i] else i

        return best

# >>> from best_time_to_buy_and_sell_stock import Solution
# >>> Solution().maxProfit([7,1,5,3,6,4])
# 5