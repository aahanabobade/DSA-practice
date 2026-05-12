# Minimum Initial Energy to Finish Tasks
# Difficulty: Hard
# Runtime: 89 ms
# Memory: 47.2 MB
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution(object):
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        ans = 0

        for actual, minimum in tasks:

            # Need more energy before starting
            if energy < minimum:
                ans += (minimum - energy)
                energy = minimum

            # Finish task
            energy -= actual

        return ans
