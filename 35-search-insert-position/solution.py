# Search Insert Position
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13 MB
# https://leetcode.com/problems/search-insert-position/

        :rtype: int
        """
        left  = 0
        right = n-1
        n = len(nums)
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] ==target :
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        
        return left

