# Product of Array Except Self
# Difficulty: Medium
# Runtime: 27 ms
# Memory: 20.3 MB
# https://leetcode.com/problems/product-of-array-except-self/


        for i in range(n-1,-1,-1):
            answer[i]*=right
            right*=nums[i]
        


            left*=nums[i]
            answer[i]=left
        for i in range(n):

        right = 1
