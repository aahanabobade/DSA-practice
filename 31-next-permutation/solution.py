# Next Permutation
# Difficulty: Medium
# Runtime: 2 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/next-permutation/

                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    break
        
        left = i+1
        right = n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
