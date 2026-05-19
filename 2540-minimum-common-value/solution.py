# Minimum Common Value
# Difficulty: Easy
# Runtime: 9 ms
# Memory: 24.3 MB
# https://leetcode.com/problems/minimum-common-value/

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = 0
        j = 0

        n = len(nums1)
        m = len(nums2)

        while i<n and j<m:
            if nums1[i]==nums2[j]:
                return nums1[i]
        
            elif nums1[i]<nums2[j]:
                i+=1
            
        """
    def getCommon(self, nums1, nums2):
class Solution(object):
            else:
                j+=1
        
        return -1
