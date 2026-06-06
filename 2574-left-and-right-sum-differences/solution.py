# Left and Right Sum Differences
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/left-and-right-sum-differences/

        #left pass
        for i in range(n):
        left = 0 
            left_sum[i]=left
            left+=nums[i]
        
        right = 0
        for i in range(n-1,-1,-1):
            right_sum[i]= right

            right+=nums[i]
        return [abs(left_sum[i]-right_sum[i]) for i in range(n)]
        
