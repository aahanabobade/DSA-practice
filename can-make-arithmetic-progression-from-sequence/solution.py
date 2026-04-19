# Q1. Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

        n = len(arr)

        arr.sort()

        dif = arr[1]-arr[0]
        for i in range(2, n):
            if arr[i]-arr[i-1]!=dif:
                return False

        return True

        
