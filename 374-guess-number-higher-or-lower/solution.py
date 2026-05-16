# Guess Number Higher or Lower
# Difficulty: Easy
# Runtime: 15 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/guess-number-higher-or-lower/

        :rtype: int
        """
        left = 1
        right = n

        while left<=right:
            mid = left+(right-left)//2

            if result ==0:
                return mid
            elif result == -1:
                right =  mid -1
            else:
                left = mid+1
            result = guess(mid)
        
