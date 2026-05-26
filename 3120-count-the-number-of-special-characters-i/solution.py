# Count the Number of Special Characters I
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

        """
        :type word: str
        :rtype: int
        """
        lower = set()
        upper = set()

        for i in word:
            if i.islower():
                lower.add(i)
            else:
                upper.add(i.lower())
        
        return len(lower & upper)

