class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            profit = sell - minBuy
            maxP = max(maxP, profit)
            minBuy = min(minBuy, sell)
        return maxP
