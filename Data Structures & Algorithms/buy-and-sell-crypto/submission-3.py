class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitMax = 0
        buyMin = prices[0]

        for sell in prices:
            profitMax = max(profitMax, sell - buyMin)
            buyMin = min(buyMin, sell)
        
        return profitMax