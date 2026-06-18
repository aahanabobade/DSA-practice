# Angle Between Hands of a Clock
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/angle-between-hands-of-a-clock/

        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour%=12

        hour_angle = hour * 30 + minutes * 0.5

        min_angle = 6*minutes

        angle = abs(hour_angle-min_angle)

        return min(angle,360-angle)
