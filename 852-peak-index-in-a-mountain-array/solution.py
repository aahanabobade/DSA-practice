# Peak Index in a Mountain Array
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 21.6 MB
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

        left = 0
        right =n-1

        while left<right:
            mid = (left+right)//2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        
        return left
