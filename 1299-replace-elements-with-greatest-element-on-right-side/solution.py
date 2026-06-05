# Replace Elements with Greatest Element on Right Side
# Difficulty: Easy
# Runtime: 54 ms
# Memory: 13.9 MB
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxx = -1
        n =  len(arr)
        
        for i in range (n-1,-1,-1):
            curr = arr[i]
            arr[i] = maxx
            maxx = max(maxx,curr)

            
        return arr