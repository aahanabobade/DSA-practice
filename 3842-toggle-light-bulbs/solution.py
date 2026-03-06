# Toggle Light Bulbs
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/toggle-light-bulbs/

class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """

        state = [False] * 101   
        
        for b in bulbs:
            state[b] = not state[b]   
        
        result = []
        for i in range(1, 101):
            if state[i]:
                result.append(i)
                
        return result
