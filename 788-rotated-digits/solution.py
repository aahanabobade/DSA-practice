# Rotated Digits
# Difficulty: Medium
# Runtime: 71 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/rotated-digits/


        for i in range(1,n+1):
            s = str(i)

            if any(d in s for d in '347'):
                continue
            
            if any(d in s for d in '2569'):
                count+=1
        
        return count
        
