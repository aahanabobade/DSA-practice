# Richest Customer Wealth
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/richest-customer-wealth/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
    
        maxx= 0
        

        for i in range(len(accounts)):  # outer loop iterates through rows 
            summ = 0 

            for j in range(len(accounts[i])): # inner loop iterates through columns
                summ = summ+accounts[i][j]
                if maxx< summ:
                    maxx = summ
        return maxx