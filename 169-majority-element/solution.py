# Majority Element
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 14.6 MB
# https://leetcode.com/problems/majority-element/


        for i in range(n):
            if count ==0:
                candidate =nums[i]
            
            if nums[i] == candidate:
        n = len(nums)
                count+=1
            else:
                count-=1
        return candidate
        candidate = None
        count = 0
        """
        :rtype: int
