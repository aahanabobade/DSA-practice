# Reverse Words in a String
# Difficulty: Medium
# Runtime: 6 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/reverse-words-in-a-string/


        while i >=0: 
            while i >=0 and s[i]==' ':
                i-=1
        
            if i<0:
                break

            j = i
            while j >= 0 and s[j]!=' ':
                j-=1
            
            result.append(s[j+1:i+1])
            i=j
            
        return " ".join(result)
