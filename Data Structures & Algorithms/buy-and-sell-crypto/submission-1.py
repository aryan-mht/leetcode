class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1

        max_profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r+=1
            else:
                p = prices[r] - prices[l]
                if p > max_profit:
                    max_profit = p
                else:
                    r+=1
        return max_profit

        