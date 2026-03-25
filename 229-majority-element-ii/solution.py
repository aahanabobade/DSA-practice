# Majority Element II
# Difficulty: Medium
# Runtime: 8 ms
# Memory: 13.9 MB
# https://leetcode.com/problems/majority-element-ii/

        
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
