# Problem Statement: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            currentProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(currentProfit,max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit