# Smallest Index With Digit Sum Equal to Index
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

        for i in range(len(nums)):
            digit_sum = 0
            num = nums[i]

            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum == i:
                return i

        return -1
