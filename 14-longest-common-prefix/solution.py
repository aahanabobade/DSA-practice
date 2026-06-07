# Longest Common Prefix
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/longest-common-prefix/

        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
