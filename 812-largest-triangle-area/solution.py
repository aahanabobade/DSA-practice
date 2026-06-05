# Largest Triangle Area
# Difficulty: Easy
# Runtime: 49 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/largest-triangle-area/

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        max_area = 0
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    
                    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
                    max_area = max(max_area, area)
        
        return max_area