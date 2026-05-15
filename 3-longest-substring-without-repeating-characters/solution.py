# Longest Substring Without Repeating Characters
# Difficulty: Medium
# Runtime: 27 ms
# Memory: 13.3 MB
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

        ans = 0

        for right in range(n):
        n = len(s)
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
        left = 0
        seen = set()
        """
            
            seen.add(s[right])
        
            ans = max(ans, right - left+1)
        return ans

