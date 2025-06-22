# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
# Date Solved: 06-22-25
# Topics: Array, Dynamic Programming

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0] # Default is set to first day's price
        profit = 0 # Tracks maximum profit
        for sell in prices[1:]:
            if sell > buy: # Runs if selling leads to a profit
                profit = max(profit, sell - buy) # Updates if profit is highest so far
            else:
                buy = sell # Updates buying price if a lower value is found
        return profit