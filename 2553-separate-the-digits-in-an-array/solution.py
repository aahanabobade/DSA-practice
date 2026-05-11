# Separate the Digits in an Array
# Difficulty: Easy
# Runtime: 16 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/separate-the-digits-in-an-array/

        for i in nums:
            
            for digit in str(i):
                ans.append(int(digit))
        
        return ans
