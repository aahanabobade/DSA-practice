# Find K Closest Elements
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 13.3 MB
# https://leetcode.com/problems/find-k-closest-elements/

        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        n = len(arr)
        right = n-k

        while left<right:
            mid = (left+right)//2

            if x- arr[mid]>arr[mid+k]-x:
                left= mid+1
            else:
                right = mid
        return arr[left:left+k]
