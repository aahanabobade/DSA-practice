# Plus One
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/plus-one/

        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            
            digits[i]=0
        
        return [1]+digits
