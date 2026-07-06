# Remove Covered Intervals
# Difficulty: Medium
# Runtime: 11 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/remove-covered-intervals/

        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end

        return count
