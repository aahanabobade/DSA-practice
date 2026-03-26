# Best Time to Buy and Sell Stock
# Difficulty: Easy
# Runtime: 83 ms
# Memory: 19.1 MB
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit
