# Valid Anagram
# Difficulty: Easy
# Runtime: 15 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/valid-anagram/

        
        for char in t:
            if char not in count:
                return False
            else: 
                count[char]-=1
                count[char]=1
            else:
                count[char]+=1
                if count[char] < 0:
                    return False
        
