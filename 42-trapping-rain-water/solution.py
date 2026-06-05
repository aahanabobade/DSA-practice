# Trapping Rain Water
# Difficulty: Hard
# Runtime: 40 ms
# Memory: 14 MB
# https://leetcode.com/problems/trapping-rain-water/


        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i-1])
        
        for i in range(n-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i+1])
        
        water = 0
        for i in range(n):
            level = min(max_left[i],max_right[i])
            water +=max(0,level-height[i])
        
        return water
