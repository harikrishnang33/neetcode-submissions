class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        high = 1
        profitMax = 0
        while high < len(prices):
            if prices[low] > prices[high]:
                low = high
            else:
                profit = prices[high] - prices[low]
                profitMax = max(profitMax, profit)
            high += 1
        
        return profitMax