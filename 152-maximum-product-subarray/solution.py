# Maximum Product Subarray
# Difficulty: Medium
# Runtime: 15 ms
# Memory: 13.1 MB
# https://leetcode.com/problems/maximum-product-subarray/

        curr_max = nums[0]
        curr_min = nums[0]
        ans= nums[0]

        for i in range(1,n):
            temp_max = max(nums[i],curr_max*nums[i],curr_min*nums[i])
            temp_min = min(nums[i],curr_max*nums[i],curr_min*nums[i])

            curr_max = temp_max
            curr_min = temp_min
        
            ans = max(curr_max, ans)

        return ans
