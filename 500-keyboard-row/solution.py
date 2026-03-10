# Keyboard Row
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/keyboard-row/

        result = []
        
        for word in words:
            w = set(word.lower())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                result.append(word)
                
        return result
