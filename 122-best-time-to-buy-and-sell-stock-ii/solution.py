# Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Runtime: 5 ms
# Memory: 13.7 MB
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]

        return profit
