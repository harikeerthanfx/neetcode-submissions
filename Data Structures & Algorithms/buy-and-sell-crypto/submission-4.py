class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        max_profit = 0

        l, r = 0 , 1
        for r in range(n):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit