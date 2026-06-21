# Maximum Ice Cream Bars
# Difficulty: Medium
# Runtime: 122 ms
# Memory: 20.7 MB
# https://leetcode.com/problems/maximum-ice-cream-bars/

        costs.sort()
        count = 0

        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break

        return count
