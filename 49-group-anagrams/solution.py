# Group Anagrams
# Difficulty: Medium
# Runtime: 23 ms
# Memory: 16.1 MB
# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grp = {}
        for i in strs:
            key = "".join(sorted(i))

            if key not in grp:
                grp[key]=[]
            
            grp[key].append(i)
        
        return list(grp.values())
