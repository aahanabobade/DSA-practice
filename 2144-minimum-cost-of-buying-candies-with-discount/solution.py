# Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)

        ans = 0
        for i in range(n):
        n = len(cost)
            if i%3!=2:
                ans+=cost[i]
        
        return ans

