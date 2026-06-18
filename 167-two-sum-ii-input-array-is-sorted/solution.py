# Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

        left = 0
        right = n - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
