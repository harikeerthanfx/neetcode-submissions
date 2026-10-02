class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0

        maxProfit = 0 
        for r in range(1,len(prices),1):
            profit  = prices[r] - prices[l]
            maxProfit = max(maxProfit,profit)

            if prices[r] < prices[l]:
                l = r
        
        return maxProfit