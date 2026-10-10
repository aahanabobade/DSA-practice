# Minimum Sum of Squared Difference
# Difficulty: Medium
# Runtime: 994 ms
# Memory: 34 MB
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

            if diff[i] > level:
                remaining -= diff[i] - level
                diff[i] = level

        # Distribute remaining operations one by one.
        # They should go to the largest equal differences.
        diff.sort(reverse=True)

        for i in range(remaining):
            diff[i] -= 1

        return sum(d * d for d in diff)
