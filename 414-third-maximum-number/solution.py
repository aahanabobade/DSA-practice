# Third Maximum Number
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/third-maximum-number/

            
            elif i > sec:
                third = sec
                sec = i
            
            elif i >third:
                third = i
        
        if third == float('-inf'):
            return first
                first = i
                sec = first
                third = sec
            if i > first:
            
                continue
