class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        
        # Option 1: Buy everything separately
        cost1_only = need1 * cost1 + need2 * cost2
        
        # Option 2: Use type 3 for the common requirement
        common = min(need1, need2)
        
        cost_mixed = (
            common * costBoth
            + (need1 - common) * cost1
            + (need2 - common) * cost2
        )
        
        # Option 3: Use type 3 for everything
        cost_all_both = max(need1, need2) * costBoth
        
        return min(cost1_only, cost_mixed, cost_all_both)