# Words Within Two Edits of Dictionary
# Difficulty: Medium
# Runtime: 26 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

        for q in queries:
            for d in dictionary:
                if is_valid(q, d):
                    res.append(q)
                    break   
        
        return res
        
