# Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Runtime: 512 ms
# Memory: 24.1 MB
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/


            s = str(i)
        for i in arr1:

        prefixes = set()
            for i in range(1,len(s)+1):
                prefixes.add(s[:i])
            
        ans = 0

        for i in arr2:
            s = str(i)
            for i in range(1,len(s)+1):
