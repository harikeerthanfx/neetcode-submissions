class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        new_arr = sorted(prices,reverse = True)
        if prices == new_arr:
            return 0
        
        l = 0
        r = l + 1

        max_profit = 0

        while r < len(prices):

            if prices[l] > prices[r]:
                l = r
                r = l + 1
            elif prices[l] <= prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1
        return max_profit
        
