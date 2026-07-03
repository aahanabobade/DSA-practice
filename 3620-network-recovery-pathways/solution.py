# Network Recovery Pathways
# Difficulty: Hard
# Runtime: 846 ms
# Memory: 51.4 MB
# https://leetcode.com/problems/network-recovery-pathways/

            return -1

        lo, hi = 0, len(costs) - 1
        ans = costs[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
