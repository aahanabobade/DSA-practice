# Earliest Finish Time for Land and Water Rides I
# Difficulty: Easy
# Runtime: 489 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

        for i in range(n):
            for j in range(m):
                arrive_at_water = landStartTime[i]+ landDuration[i]
                finish_order1 = max(arrive_at_water, waterStartTime[j]) + waterDuration[j]

                arrive_at_land = waterStartTime[j] + waterDuration[j]
                finish_order2 = max(arrive_at_land, landStartTime[i] )+ landDuration[i]

                ans = ans = min(ans, finish_order1, finish_order2)
        return ans


        m = len(waterStartTime)
