# Earliest Finish Time for Land and Water Rides II
# Difficulty: Medium
# Runtime: 1226 ms
# Memory: 33.6 MB
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

        pre_min_dur = [0] * m
        pre_min_dur[0] = wDur[0]
        for i in range(1, m):
        m = len(water)

        # prefix min of duration (for rides already open)
        wDur   = [w[1] for w in water]
        water = sorted(zip(waterStartTime, waterDuration))
        wStart = [w[0] for w in water]
        
    waterDuration):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, 
class Solution(object):

import bisect
