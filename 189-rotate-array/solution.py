# Rotate Array
# Difficulty: Medium
# Runtime: 7 ms
# Memory: 22.2 MB
# https://leetcode.com/problems/rotate-array/

            end-=1

        start =0
        end = n-1
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    
            start+=1
