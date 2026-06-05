# Integer to Roman
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/integer-to-roman/

        :type num: int
        :rtype: str
        """
        values  = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        n = len(values)
        result = ""

        for i in range(n):
            while num>=values[i]:
                result+=symbols[i]
                num-=values[i]
        
        return result

